from sqlmodel import SQLModel
from uuid import UUID
from pydantic import EmailStr
from datetime import datetime

class UserBase(SQLModel):
    id_user: UUID = None
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime = None

