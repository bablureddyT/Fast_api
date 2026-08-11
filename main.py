from fastapi import FastAPI,APIRouter
from typing import Generic, TypeVar,Optional
from dataclasses import dataclass
from pydantic import BaseModel
from routers.userrouters import router as user_router
from database.database import Base,engine

app = FastAPI()

from dataclasses import dataclass

app.include_router(user_router)

Base.metadata.create_all(bind=engine)

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

# @app.post


