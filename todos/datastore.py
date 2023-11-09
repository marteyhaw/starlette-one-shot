from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

import settings

client = MongoClient(settings.MONGO_URL)
db = client[settings.MONGO_DB]


# Create a to-do list
def create_todo_list(todo_list):
    todo_list["_id"] = todo_list["name"]
    todo_list["id"] = ObjectId()
    todo_list["created_on"] = datetime.now().isoformat()
    new_todo_list = db["todo_lists"].insert_one(todo_list)
    created_todo_list = db["todo_lists"].find_one({"_id": new_todo_list.inserted_id})
    return created_todo_list


# Get a to-do list's items
def get_todo_lists_items(todo_list_id):
    todo_lists_items = list(db["todo_items"].find({"list": todo_list_id}))
    return todo_lists_items


# Get a list of to-do lists including their to-do items
def get_todo_lists():
    todo_lists = list(db["todo_lists"].find())
    for todo_list in todo_lists:
        todo_list["todo_items"] = get_todo_lists_items(todo_list["_id"])
    return todo_lists


# Get the details of a to-do list
def get_todo_list(todo_list_id):
    todo_list = db["todo_lists"].find_one({"id": todo_list_id})
    return todo_list


# Edit a to-do list
def edit_todo_list(todo_list_id, todo_list):
    update_result = db["todo_lists"].update_one(
        {"id": todo_list_id}, {"$set": todo_list}
    )
    return update_result


# Delete a to-do list
def delete_todo_list(todo_list_id):
    todo_list = db["todo_lists"].find_one({"id": todo_list_id})
    db["todo_items"].delete_many({"list": todo_list["_id"]})
    delete_result = db["todo_lists"].delete_one({"id": todo_list_id})
    return delete_result


# Create a to-do item
def create_todo_item(todo_item):
    todo_item["_id"] = str(ObjectId())
    new_todo_item = db["todo_items"].insert_one(todo_item)
    created_todo_item = db["todo_items"].find_one({"_id": new_todo_item.inserted_id})
    return created_todo_item


# Get the details of a to-do item
def get_todo_items():
    todo_items = list(db["todo_items"].find())
    return todo_items
