from typing import Dict, List

from fastapi import APIRouter, Body, Query, Request
from fastapi.encoders import jsonable_encoder

from ..utils import (
    add_item,
    retrieve_items,
    retrieve_item_by_id,
    retrieve_item_by_filter,
)
from ..models.item import (
    error_response_model,
    response_model,
    ItemSchema,
)

router = APIRouter()


@router.post("/", description="Add new item")
async def add_item_data(item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    if new_item:
        return response_model(new_item, "Item added successfully.")
    return error_response_model("An error occurred.", 404, "item already exist.")


@router.get("/", description="Return data of all items")
async def get_items():
    items = await retrieve_items()
    if items:
        return response_model(items, "Items data retrieved successfully")
    return response_model(items, "Empty list returned")


@router.get("/{item_id}", description="Return item by ID")
async def get_items_by_id(item_id: int = Query(...)):
    item = await retrieve_item_by_id(item_id)
    if item:
        return response_model(item, "Item data retrieved successfully by ID")
    return response_model(item, "Empty list returned")


@router.get("/filter_by", description="Return items filtered by")
async def get_items_by_filter(filter: str = Query(default='key'), value: str = Query(default='value')):
    item = await retrieve_item_by_filter(filter, value)
    if item:
        return response_model(item, "Item data retrieved successfully by ID")
    return response_model(item, "Empty list returned")
