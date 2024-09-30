from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
  item: str

items: List[Item] = [Item(item="ali")]

@app.get("/", response_model=List[Item])
def root():
  return items

@app.post("/items", response_model=List[Item])
def create_item(item: Item):
  items.append(item)
  return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
  if item_id < 0 or item_id >= len(items):
      raise HTTPException(status_code=404, detail="Item not found")
  return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
  if item_id < 0 or item_id >= len(items):
      raise HTTPException(status_code=404, detail="Item not found")
  items[item_id] = item
  return item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
  if item_id < 0 or item_id >= len(items):
      raise HTTPException(status_code=404, detail="Item not found")
  return items.pop(item_id)