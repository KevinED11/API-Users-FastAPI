from sqlmodel import SQLModel
from pydantic import EmailStr
class UpdateUser(SQLModel):
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str




