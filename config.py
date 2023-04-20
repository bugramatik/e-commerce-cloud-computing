import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'your-mongodb-atlas-connection-string'
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME') or 'your-database-name'
