import os
import pymongo


DB_NAME = os.getenv("DB_NAME")
CLIENT = pymongo.MongoClient("mongodb://db:27017")
db = CLIENT[DB_NAME]


def get(model, _id):
    table = model.table_name
    return db[table].find_one(_id)


def post(instance):
    table = instance.table_name
    return db[table].insert(instance.to_dict())
