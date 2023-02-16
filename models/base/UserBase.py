from sqlmodel import SQLModel, Field
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from uuid import UUID
from typing import Optional
from pydantic import EmailStr, validator
from datetime import datetime
from enum import Enum


class UserBase(SQLModel):
    id_user: Optional[UUID] = None
    name: str = Field(index=True)
    surname: str
    username: str
    age: int = Field(index=True)
    email: EmailStr
    password: str
    created_at: Optional[datetime] = None
    #roles: list[Roles]

    @validator('age')
    def validate_age(cls, v):
        if v < 18:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid age, place 18 or more")
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 12:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Place 12 or more characters")
        return v







