from fastapi import APIRouter
from backend.models.read.UserRead import UserRead
from backend.config.db_connection import engine
from sqlmodel import Session
from backend.models.database.Users import Users
from backend.exceptions.exception_handlers import raise_404_not_found

find_by_id = APIRouter(tags=['Users'])


@find_by_id.get('/users/id/{user_id}', response_model=UserRead, response_description='User found')
async def get_user_by_id(user_id: int) -> Users:
    with Session(engine) as session:
        user: Users = session.get(Users, user_id)

        if user:
            return user
        raise_404_not_found(detail="User not found")
