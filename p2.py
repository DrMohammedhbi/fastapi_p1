
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    item: str
items = [   Item(item="ali")    ]

@app.get("/")
def root():
    # return {"Hello": "World"}
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item.item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item= items[item_id]
    return item

