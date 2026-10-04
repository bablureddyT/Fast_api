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
