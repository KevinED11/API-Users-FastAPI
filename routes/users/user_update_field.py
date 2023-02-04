from fastapi import APIRouter, HTTPException
from typing import Optional
from routes.users.user_find import UUID
from routes.users.root_get import users_id_dict, users_ls

userUpdateField = APIRouter()

@userUpdateField.patch('/users/{user_id}', response_model=None, status_code=200)
async def field_update(user_id: UUID, name: Optional[str] = None, surname: Optional[str] = None, email: Optional[str] = None ):
    if user_id not in users_id_dict:
        raise HTTPException(status_code=404, detail=f'user with ID {user_id} not found')

    user = users_id_dict[user_id]

    if name:
        user.name = name
    if surname:
        user.surname = surname
    if email:
        user.email = email


    users_ls.append(user)
    users_id_dict[user.id_user] = user





