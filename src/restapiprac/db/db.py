from ..schemas.items import CreateItem
from fastapi import FastAPI

datasets = [
    {"id": 1, "category": "Earth", "size": 250},
    {"id": 2, "category": "Space", "size": 500},
    {"id": 3, "category": "Earth", "size": 150},
    {"id": 4, "category": "Space", "size": 300},
]


def read_root():
    return {"Hello" : "World"}

def read_all_items():
    if datasets:
        return datasets
    return None

def read_item(id:int):
    for obj in datasets:
        if obj["id"] == id:
            return obj
    return None

def add_item(item:CreateItem):
    prev = len(datasets)
    datasets.append({"id": item.id, "category": item.category, "size": item.size})
    if prev < len(datasets):
        return True
    return False

def delete_item(id:int):
    length = len(datasets)
    for i in range(length):
        if datasets[i]["id"] == id:
            del datasets[i]
            return True
    return False
    