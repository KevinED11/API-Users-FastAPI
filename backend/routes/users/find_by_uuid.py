from fastapi import APIRouter
from backend.models.read.UserRead import UserRead
from uuid import UUID
from backend.config.db_connection import engine
from sqlmodel import Session, select
from backend.models.database.Users import Users
from backend.exceptions.exception_handlers import raise_404_not_found

find_by_uuid = APIRouter(tags=['Users'])


@find_by_uuid.get('/users/{user_uuid}', response_model=UserRead, response_description='User found')
async def get_user_by_uuid(user_uuid: UUID) -> Users:
    with Session(engine) as session:

        user = session.exec(select(Users)
                            .where((Users.id_user == user_uuid))
                            ).one_or_none()

        if user:
            return user
        raise_404_not_found(detail="User not found")
