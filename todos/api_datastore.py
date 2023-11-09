from bson import ObjectId
from pymongo import MongoClient

import settings

client = MongoClient(settings.MONGO_URL)
db = client[settings.MONGO_DB]


def create_todo_item(todo_item):
    todo_item["_id"] = str(ObjectId())
    new_todo_item = db["todo_items"].insert_one(todo_item)
    created_todo_item = db["todo_items"].find_one({"_id": new_todo_item.inserted_id})
    return created_todo_item


def list_todos():
    todo_items = list(db["todo_items"].find())
    for todo_item in todo_items:
        for k, v in todo_item.items():
            if k == "created_on":
                todo_item[k] = v.isoformat()
    return todo_items
