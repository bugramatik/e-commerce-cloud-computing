from pymongo.mongo_client import MongoClient
import config


# Create a new client and connect to the server
uri = config.MONGO_URI
db = config.MONGO_DB

def connect_to_db():
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
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