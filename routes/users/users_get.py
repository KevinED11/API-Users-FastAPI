from routes.users.root_get import *
from typing import Optional, List
from models.User import User


usersGet = APIRouter()

users_ls: List[User] = [


]

@usersGet.get('/users', response_model = List[User])
async def get_users(name: Optional[str] = None, age: Optional[int] = None):
    filtered_users = users_ls
    if name and age:
        filtered_users = [user for user in filtered_users if user.name == name and user.age == age]
    elif name:
        filtered_users = [user for user in filtered_users if user.name == name]
    elif age:
        filtered_users = [user for user in filtered_users if user.age == age]

    return filtered_users