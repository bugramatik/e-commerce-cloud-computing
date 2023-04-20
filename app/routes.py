from app import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
def index():
    categories = ["Clothing", "Computer Components", "Monitors", "Snacks"]
    return render_template('index.html', categories=categories)
