from fastapi import APIRouter, HTTPException
from models.read.UserRead import UserRead
from uuid import UUID
from sqlmodel import Session, select
from models.database.Users import Users
from config.db_connection import engine
from starlette.status import HTTP_404_NOT_FOUND
userFind = APIRouter(tags=['Users'])

@userFind.get('/users/{user_id}', response_model = UserRead, response_description='User found')
async def get_user_by_id(user_id: UUID):
    with Session(engine) as session:
        #Search user by id in db
        user = session.exec(select(Users).where(Users.id_user == user_id)).one_or_none()

        if user:
            return user
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")


