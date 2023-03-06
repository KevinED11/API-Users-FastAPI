from fastapi import APIRouter, Query
from backend.models.read.UserRead import UserRead
from backend.models.database.Users import Users
from backend.config.db_connection import engine
from sqlmodel import Session, select

users_get = APIRouter(tags=['Users'])


@users_get.get('/users', response_model=list[UserRead], status_code=200)
async def get_users(offset: int = 0, limit: int = Query(default=10, le=100)) -> list[Users]:
    offset = max(0, offset)

    with Session(engine) as session:
        #Users returned
        return session.exec(select(Users).offset(offset).limit(limit)).all()





