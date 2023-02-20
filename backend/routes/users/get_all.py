from fastapi import APIRouter, HTTPException, Query
from backend.models.read.UserRead import UserRead
from backend.models.database.Users import Users
from backend.config.db_connection import engine
from sqlmodel import Session, select

usersGet = APIRouter(tags = ['Users'])

@usersGet.get('/users', response_model=list[UserRead], status_code=200)
async def get_users(offset: int = 0, limit: int = Query(default=10, le=100)) -> list[Users]:
    #if offset < 0:
     #   offset = abs(offset)
    offset = max(0, offset)

    with Session(engine) as session:
        #Users returned
        return session.exec(select(Users)
                            .offset(offset)
                            .limit(limit)
                            ).all()





