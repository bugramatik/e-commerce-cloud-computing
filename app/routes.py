#TODO: unique username, item name, category name
#TODO: Rate review implement et
#TODO: indexde itemlerin listelenmesi isteniyo
#TODO: Authoritazion bidaha kontrol et
#TODO: Dynamic schema olayina bi bakmak lazim gereksiz field kullanmamak lazim computer icin size gibi
#TODO: User remove edilince itemler de silinmeli, rate reviewlar da silinmeli
#TODO: User list rewiev rate gozukmeli,

from app import app
from flask import render_template,request,redirect,url_for,flash,session
from pymongo.mongo_client import MongoClient
from bson import ObjectId
from .db import *
import bcrypt


client = connect_to_db()


@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    username = request.form['username']
    password_to_check = request.form.get('password').encode('utf-8')
    user = get_user(username)

    if user:
        hashed_password_from_db = user['password'].encode('utf-8')
        if bcrypt.checkpw(password_to_check, hashed_password_from_db):
            session['username'] = user['username']
            session['is_admin'] = user['is_admin']
            flash('Successfully logged in', 'success')
            return redirect(url_for('index'))
        flash('Incorrect password', 'error')
        return redirect(url_for('index'))
    else:
        flash('User not found', 'error')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index.html')
def index():
    categories = [ category['name'] for category in client.get_collection('categories').find()]
    # items = client.get_collection('items').find()
    return render_template('index.html', categories=categories,session=session)


@app.route('/search_results.html', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        selected_categories = request.form.getlist('categories')

        items_collection = client.get_collection('items')

        search_filter = {'category': {'$in': selected_categories}}

        results = items_collection.find(search_filter)
        print(results)

        return render_template('search_results.html', results=results)
    else:
        return redirect('/index.html')


@app.route('/list_items.html')
def list_items():
    items = list(client.get_collection('items').find())
    users = client.get_collection('users').find()
    users_dict= {str(user['_id']):user['username'] for user in users}
    categories = client.get_collection('categories')
    for item in items:
        category = categories.find_one({'_id': ObjectId(item['category'])})
        item['category_name'] = category['name']
    return render_template('list_items.html', items=items,users_dict=users_dict)


@app.route('/add_item.html', methods=['GET', 'POST'])
def add_item():
    if session.get('is_admin'):
        categories = list(client.get_collection('categories').find())
        users = list(client.get_collection('users').find())
        users = [user for user in users if user['is_admin'] == False]
        if request.method == 'POST':
            item_data = {
            'name': request.form['name'],
            'category': request.form['category'],
            'description': request.form['description'],
            'price': float(request.form['price']),
            'seller': request.form['seller'],
            'image_url': request.form['image_url'],
            'rating': 0,
            'reviews': [],
            'details': {
                'size': request.form.get('size', None),
                'colour': request.form.get('colour', None),
                'spec': request.form.get('spec', None),
                }
            }

            client.get_collection('items').insert_one(item_data)
            flash('Item added successfully', 'success')
            return redirect(url_for('list_items'))
        print(users)
        return render_template('add_item.html', categories=categories, users=users)
    else:
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('index'))

@app.route('/item/<item_id>')
def item_details(item_id):
    item = client.get_collection('items').find_one({'_id': ObjectId(item_id)})
    users_dict = {str(user['_id']):user['username'] for user in client.get_collection('users').find()}
    categories = client.get_collection('categories')
    category = categories.find_one({'_id': ObjectId(item['category'])})
    item['category_name'] = category['name']

    return render_template('item_details.html', item=item,users_dict=users_dict)


@app.route('/submit_review/<item_id>', methods=['POST'])
def submit_review(item_id):
    rating = int(request.form['rating'])
    review = request.form['review']
    username = session['username']

    # client.get_collection('items').update_one({}

    flash('Review submitted successfully', 'success')
    return redirect(url_for('item_details', item_id=item_id))


@app.route('/list_users.html')
def list_users():
    if session.get('is_admin'):
        users = client.get_collection('users').find()
        return render_template('list_users.html', users=users,session=session)
    else:
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('index'))


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    if session.get('is_admin'):
        result = client.get_collection('items').delete_one({'_id': ObjectId(item_id)})
        if result.deleted_count == 1:
            flash('Item successfully deleted', 'success')
        else:
            flash('Item not found', 'error')
    else:
        flash('You do not have permission to delete items', 'error')
    return redirect(url_for('list_items'))


@app.route('/add_user.html', methods=['GET', 'POST'])
def add_user():
    if not session.get('is_admin'):
        flash('Access denied', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_admin = request.form.get('is_admin') == 'on'

        # Check if the username already exists
        existing_user = get_user(username)
        if existing_user:
            flash('Username already exists', 'error')
            return redirect(url_for('add_user'))

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user and save it to the database
        user = {
            'username': username,
            'password': hashed_password.decode('utf-8'),
            'is_admin': is_admin
        }
        client.get_collection('users').insert_one(user)
        flash('User added successfully', 'success')
        return redirect(url_for('list_users'))

    return render_template('add_user.html')


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    if session.get('is_admin'):
        result = client.get_collection('users').delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            flash('User successfully deleted', 'success')
        else:
            flash('User not found', 'error')
    else:
        flash('You do not have permission to delete users', 'error')
    return redirect(url_for('list_users'))

