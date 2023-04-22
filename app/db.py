from pymongo.mongo_client import MongoClient

import config

uri = config.MONGO_URI
db = config.MONGO_DB


def connect_to_db():
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
    except Exception as e:
        print("Could not connect to MongoDB: %s" % e)

    return client[db]


def get_user(username):
    client = connect_to_db()
    users_collection = client.get_collection('users')
    user = users_collection.find_one({'username': username})
    return user
