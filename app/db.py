import os
import pymongo


DB_NAME = os.getenv("DB_NAME")
CLIENT = pymongo.MongoClient("mongodb://db:27017")
db = CLIENT[DB_NAME]


def get(model, _id):
    table = model._table_name
    return model.parse_obj(db[table].find_one(_id))

def post(instance):
    table = instance.table_name
    return db[table].insert(instance.dict() | {"_id": instance._id.hex})
