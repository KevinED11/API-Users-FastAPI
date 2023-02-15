from models.base.UserBase import UserBase
from sqlmodel import Field
from typing import Optional
class Users(UserBase, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)










