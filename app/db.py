from pymongo.mongo_client import MongoClient

# Create a new client and connect to the server
uri = "mongodb+srv://ergenekonsahin:Deneme123@cluster0.tigmchw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)


def connect_to_db():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
    except Exception as e:
        print(e)
    return client