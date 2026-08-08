from fastapi import FastAPI
from typing import Generic, TypeVar,Optional
from dataclasses import dataclass
from pydantic import BaseModel

app = FastAPI()

from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    username: str
    age: int | None = None
    age: int | None = None # even they are two same 

    
    
@dataclass
class Item:
    name:str
    age: int | None = None

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
def getItem(item_id:int):
    item =Item(name=item_id)
    return {"item": "empty"}

@app.get("/items/{item_id}")
def getItem(item_id:str):
    item =Item(name=item_id)
    return {"item": item.name}

# @app.post


