from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(f"mongodb://localhost:27017/")

    db = client.HW_Web_10
    return db
