from fastapi import APIRouter, HTTPException
from models.read.UserRead import UserRead
from uuid import UUID
from config.db_connection import engine
from sqlmodel import Session, select
from models.database.Users import Users
from starlette.status import HTTP_404_NOT_FOUND

findByUuid = APIRouter(tags=['Users'])

@findByUuid.get('/users/{user_uuid}', response_model=UserRead, response_description='User found')
async def get_user_by_uuid(user_uuid: UUID) -> Users:
    with Session(engine) as session:

        user = session.exec(select(Users)
                            .where( (Users.id_user == user_uuid) )
                            ).one_or_none()

        if user:
            return user
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")


