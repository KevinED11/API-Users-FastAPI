from sqlmodel import SQLModel
from typing import Optional
from pydantic import EmailStr

class UpdateFields(SQLModel):
    name: Optional[str | None] = None
    surname: Optional[str | None] = None
    username: Optional[str | None] = None
    age: Optional[int | None] = None
    email: Optional[EmailStr | None] = None
    password: Optional[str | None] = None




