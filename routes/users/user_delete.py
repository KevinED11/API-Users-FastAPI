from fastapi import APIRouter, Response
from config.db_connection import engine
from sqlmodel import Session, select
from models.database.Users import Users
from uuid import UUID

userDelete = APIRouter(tags=['Users'])

@userDelete.delete('/users/{user_id}', response_model = None, status_code=204, response_description='User deleted')
async def delete_user(user_id: UUID):
    with Session(engine) as session:
        all_users = session.exec(select(Users)).all()
        for user in all_users:
            if user.id_user == user_id:
                session.delete(user)
                session.commit()
                return Response(content=None, status_code=204)


