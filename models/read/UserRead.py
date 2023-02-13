from models.base.UserBase import UserBase
from pydantic import Required

class UserRead(UserBase):
    id: int = Required