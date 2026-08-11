from pydantic import BaseModel

class UserSchema(BaseModel):
    # id:int
    user_id:int
    name:str
    email:str=""
    age:int|None=None