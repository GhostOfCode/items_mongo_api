from pymongo import MongoClient

from .config import MONGO_DETAILS

client = MongoClient(MONGO_DETAILS)

#  Collection items_collection as a DBS items will be automatically created by first execution of request
database = client.items
item_collection = database.get_collection("items_collection")


def item_helper(item) -> dict:
    return {
        'db_id': str(item['_id']),
        "item_id": item["item_id"],
        "item_name": item["item_name"],
        "description": item["description"],
        "spec": item["spec"],
    }


# Add a new item into the database
async def add_item(item_data: dict) -> dict:
    item_old = item_collection.find_one({"item_id": item_data['item_id']})
    if item_old:
        return {'error': 'an item with that item_id already exist'}
    item = item_collection.insert_one(item_data)
    new_item = item_collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)


# Retrieve all items present in the database
async def retrieve_items():
    items = []
    for item in item_collection.find():
        items.append(item_helper(item))
    return items


# Retrieve item data by item_id
async def retrieve_item_by_id(item_id):
    item = item_collection.find_one({'item_id': item_id})
    return item_helper(item)


# Retrieve items data by filter
async def retrieve_item_by_filter(filter, value):
    items = []
    for item in item_collection.find({filter, value}):
        items.append(item_helper(item))
    return items
