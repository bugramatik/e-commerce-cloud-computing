from app import app
from flask import render_template,request,redirect
from pymongo.mongo_client import MongoClient
from .db import *

client = connect_to_db()

@app.route('/')
@app.route('/index.html')
def index():
    categories = [ category['name'] for category in client.get_collection('categories').find()]
    items = client.get_collection('items').find()
    for item in items:
        print(item)
    return render_template('index.html', categories=categories)



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


