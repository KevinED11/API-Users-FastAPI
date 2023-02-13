from fastapi import APIRouter, HTTPException
from models.read.UserRead import UserRead
from models.database.Users import Users
from config.db_connection import engine
from sqlmodel import Session, select
usersGet = APIRouter(tags=['Users'])

@usersGet.get('/users', response_model=list[UserRead], status_code=200)
async def get_users(name: str | None = None, age: int | None = None):

    with Session(engine) as session:
        users = session.exec(select(Users)).all()
        #query_selection = select(Users)
        #result = session.exec(query_selection)
        #users = result.all()


        if name and age:
            users = [user for user in users if user.name == name and user.age == age]

            return users

        elif name:
            users = [user for user in users if user.name == name]
            return users
        elif age:
            users = [user for user in users if user.age == age]
            return users


        return users



