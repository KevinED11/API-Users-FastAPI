from fastapi import APIRouter, HTTPException, Query
from models.read.UserRead import UserRead
from models.database.Users import Users
from config.db_connection import engine
from sqlmodel import Session, select

usersGet = APIRouter(tags=['Users'])

@usersGet.get('/users', response_model=list[UserRead], status_code=200)
async def get_users(offset: int = 0, limit: int = Query(default=10, le=100)):
    if offset < 0:
        offset = abs(offset)

    with Session(engine) as session:
        #Users returned
        return session.exec(select(Users).offset(offset).limit(limit)).all()




