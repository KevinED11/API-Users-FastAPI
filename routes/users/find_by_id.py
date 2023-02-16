from fastapi import APIRouter, HTTPException
from models.read.UserRead import UserRead
from config.db_connection import engine
from sqlmodel import Session
from models.database.Users import Users
from starlette.status import HTTP_404_NOT_FOUND

findById = APIRouter(tags=['Users'])

@findById.get('/users/id/{user_id}', response_model = UserRead, response_description='User found')
async def get_user_by_id(user_id: int):
    with Session(engine) as session:

        user = session.get(Users, user_id)

        if user:
            return user
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

