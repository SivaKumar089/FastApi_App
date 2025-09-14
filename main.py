from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: Optional[bool] = True


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# ✅ fixed: use query params and return an Item model
@app.get("/items/", response_model=Item)
def get_items(name: str, price: float, in_stock: Optional[bool] = True):
    return Item(name=name, price=price, in_stock=in_stock)


@app.get("/search/")
def search_items(q: str = None):
    return {"query": q}


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
