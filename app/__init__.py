from flask import Flask

import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
from app import routes
