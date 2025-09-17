from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel,Field

app = FastAPI()

# Pydantic model for request body
class Item(BaseModel):
    name: str =Field(...,min_length=2,max_length=50)
    price: float =Field(...,gt=0)
    in_stock:bool= True


# Fake database
items = {}

@app.get('/')
def home():
    return {"message": "Hello, FastAPI!"}

# 1️⃣ GET - Read all items
@app.get("/items", status_code=status.HTTP_200_OK)
def get_items():
    return items


# 2️⃣ GET - Read one item
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item_id": item_id, "item": items[item_id]}


# 3️⃣ POST - Create a new item
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"message": "Item created", "item_id": item_id, "item": item}


# 4️⃣ PUT - Update an item (replace it fully)
@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated", "item_id": item_id, "item": item}


# 5️⃣ DELETE - Remove an item
@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": "Item deleted", "deleted_item": deleted_item}
