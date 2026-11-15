from fastapi import APIRouter, Depends, HTTPException,status
from restapiprac.db.db import read_all_items, add_item, read_item, delete_item, patch_item
from restapiprac.schemas.items import CreateItem, ItemResponse

router = APIRouter(prefix="/item")

@router.get("/", status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def get_items():
    res = read_all_items()
    if res:
        raise HTTPException(status_code=404, detail="Could not get items")
    return res

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def get_item(id:int):
    res = read_item(id)
    if res:
        raise HTTPException(status_code=404, detail="Could not get item")
    return res

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
async def add(item:CreateItem):
    res = add_item(item)
    if not res:
        raise HTTPException(status_code=422, detail="Could not add duplicate item with duplicate id")
    return {"item": item}

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def patched(id: int, item:CreateItem):
    res = patch_item(id, item)
    if not res:
        raise HTTPException(status_code=422, detail="Could not patch item")
    return res

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete(id:int):
    if not delete_item(id):
        raise HTTPException(status_code=404, detail="Could add item")
    return
