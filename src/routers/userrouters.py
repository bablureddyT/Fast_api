from fastapi import APIRouter,FastAPI,BackgroundTasks,HTTPException,Depends
from dataclasses import dataclass
from database.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.user_db import User
from schemas.user_schema import UserSchema

router=APIRouter()

@router.get("/")
def home():
    return {"message": "Hello FastAPI"}

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    data = db.get(User, user_id)
    if data is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return data

@router.get("/user_email/{email}")
def find_user_by_email(email:str,db=Depends(get_db)):
    statement = select(User).where(
    User.email == email)
    result = db.execute(statement)
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.post("/users")
def get_users(data:UserSchema,db:Session=Depends(get_db)):
    try:
        user = User(**data.model_dump())
        db.add(user)
        db.flush()
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    # finally:
    #     db.close()




# @router.get("/items/{item_id}")
# def getItem(item_id:int):
#     item =Item(name=item_id)
#     return {"item": "empty"}

# @router.get("/items/{item_id}")
# def getItem(item_id:str):
#     item =Item(name=item_id)
#     return {"item": item.name}

