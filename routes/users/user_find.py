from routes.users.users_get import *
from models.User import *
from fastapi import HTTPException
from typing import Dict

userFind = APIRouter()

users_id_dict: Dict[UUID, User] = {


}
@userFind.get('/users/{user_id}', response_model = User, response_description='User found')
async def get_user_by_id(user_id: UUID):
    if user_id in users_id_dict:
        return users_id_dict[user_id]
    else:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')