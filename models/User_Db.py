from sqlmodel import SQLModel, Field
from uuid import UUID
from typing import Optional
from pydantic import EmailStr
from datetime import datetime
class NewUser(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key=True)
    id_user: UUID
    name: str
    surname: str
    username: str
    age: int
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime



