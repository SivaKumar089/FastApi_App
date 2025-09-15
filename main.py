from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    email: str

# In-memory storage
users = []

# GET API
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return users

# POST API
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}