from backend.models.base.UserBase import UserBase
from sqlmodel import Field
from typing import Optional
from enum import Enum
class Roles(Enum):
    USER = "user"
    PREMIUM = "premium"
    ADMIN = "admin"

class Users(UserBase, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)
    #roles: list[Roles]







