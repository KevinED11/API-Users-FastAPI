from sqlmodel import SQLModel
from pydantic import EmailStr

class UpdateFields(SQLModel):
    name: str = None
    surname: str = None
    username: str = None
    age: int = None
    email: EmailStr = None
    password: str = None




