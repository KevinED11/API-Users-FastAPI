from fastapi import APIRouter, HTTPException, Query, Path, Body
from pydantic import EmailStr
from uuid import UUID
from routes.users.root_get import users_id_dict, users_ls
userUpdateField = APIRouter()

@userUpdateField.patch('/users/{user_id}', response_model=None, status_code=200)
async def field_update(user_id: UUID,
                       name: str | None = Query(default = None, max_length = 15),
                       username: str | None = Query(default = None, max_length = 15) ,
                       surname: str | None = Query(default = None, max_length = 15),
                       email: EmailStr | None = Query(default = None)
                       ):

    if user_id not in users_id_dict:
        raise HTTPException(status_code=404, detail=f'user with ID {user_id} not found')

    user = users_id_dict[user_id]

    if name:
        user.name = name
    if username:
        user.username = username
    if surname:
        user.surname = surname
    if email:
        user.email = email

    users_id_dict[user_id] = user

    for i, existing_user in enumerate(users_ls):
        if user_id == existing_user.id_user:
            users_ls[i] = user





