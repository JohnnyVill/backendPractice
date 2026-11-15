from fastapi import APIRouter, Depends, HTTPException
from restapiprac.db.db import read_all_items, add_item, read_item, delete_item
from restapiprac.schemas.items import CreateItem

router = APIRouter(prefix="/items")

@router.get("/")
async def get_items():
    if read_all_items():
        return read_all_items()
    return "Nothing"

@router.get("/{id}")
async def get_item(id:int):
    res = read_item(id)
    if res:
        return res
    return "Does not exist"

@router.post("/add")
async def add(item:CreateItem):
    if add_item(item):
        return "Successfully added"
    return "Error Occured"

@router.delete("/delete")
async def delete(id:int):
    if delete_item(id):
        return "Successfully deleted"
    return "Could not delete"
