from fastapi import APIRouter, HTTPException
from typing import List
from ..models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# In-memory storage
items = []

@router.get("/", response_model=List[Item])
async def get_items():
    return items

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_index] = updated_item
    return updated_item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items.pop(item_index)
    return {"message": "Item deleted successfully"} 
    return {"message": "Item deleted successfully"} 