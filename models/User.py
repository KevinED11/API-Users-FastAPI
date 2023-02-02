from pydantic import BaseModel, EmailStr
from uuid import uuid4, UUID
from datetime import datetime

class User(BaseModel):
    id: UUID
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime

    # @validator("age")
    # def validate_age(cls, age):
    #   if age < 18:
    #      raise HTTPException(status_code=400, detail="Place age more than 18 characters")
    # @validator("password")
    # def validate_password(cls, v):
    #   if len(v) < 12:
    #      raise ValueError('Place 12 or more characters')
    # return v