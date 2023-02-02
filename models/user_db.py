from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from config.db_connection import engine, meta_data
from uuid import UUID
from datetime import datetime

class Users(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime

#meta_data.metadata.create_all(engine)
SQLModel.metadata.create_all(engine)
