from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient('mongodb://localhost')
    return client.hw10
