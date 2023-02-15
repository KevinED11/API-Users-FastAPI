from sqlmodel import SQLModel, Field
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from uuid import UUID
from typing import Optional
from pydantic import EmailStr, validator
from datetime import datetime

class UserBase(SQLModel):
    id_user: Optional[UUID] = None
    name: str = Field(index=True)
    surname: str
    username: str
    age: int = Field(index=True)
    email: EmailStr
    password: str
    created_at: Optional[datetime] = None







