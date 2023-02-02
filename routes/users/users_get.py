from routes.users.root_get import *
from fastapi import HTTPException
from models.User import User
from typing import Optional, List



usersGet = APIRouter()



@usersGet.get('/users', response_model = List[User])
async def get_users(name: Optional[str] = None, age: Optional[int] = None):
    if age is not None and age < 18:
        raise HTTPException(status_code=400, detail='Place a age > 17')

    filtered_users: List[User] = users_ls
    if name and age:
        filtered_users = [user for user in filtered_users if user.name == name and user.age == age]
    elif name:
        filtered_users = [user for user in filtered_users if user.name == name]
    elif age:
        filtered_users = [user for user in filtered_users if user.age == age]

    return filtered_users