from fastapi import APIRouter
from models.request.User import User
from uuid import UUID
from sqlmodel import Session, select
from models.database.User import Users
from config.db_connection import engine

userFind = APIRouter()

@userFind.get('/users/{user_id}', response_model = User, response_description='User found')
async def get_user_by_id(user_id: UUID):
    with Session(engine) as session:
        users = session.exec(select(Users)).all()

        for user in users:
            if user.id_user == user_id:
                return user

