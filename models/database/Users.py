from sqlmodel import Field
from typing import Optional
from models.base.UserBase import UserBase
class Users(UserBase, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)










