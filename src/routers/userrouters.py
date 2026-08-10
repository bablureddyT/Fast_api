from fastapi import APIRouter,FastAPI,BackgroundTasks,HTTPException,Depends
from dataclasses import dataclass
# from app import 

router=APIRouter()

# def get_db():

@router.get("/")
def home():
    return {"message": "Hello FastAPI"}

@router.get("/items/{item_id}")
def getItem(item_id:int):
    item =Item(name=item_id)
    return {"item": "empty"}

@router.get("/items/{item_id}")
def getItem(item_id:str):
    item =Item(name=item_id)
    return {"item": item.name}

@router.get("/users")
def get_users():
    return ""

