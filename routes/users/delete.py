from fastapi import APIRouter, Response, HTTPException
from config.db_connection import engine
from sqlmodel import Session, select
from models.database.Users import Users
from uuid import UUID
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

userDelete = APIRouter(tags = ['Users'])

@userDelete.delete('/users/{user_id}', response_model=None, status_code=204, response_description='User deleted')
async def delete_user(user_id: UUID) -> Response:
    with Session(engine) as session:

        user_to_delete: Users | None = session.exec(select(Users)
                                                    .where( (user_id == Users.id_user) )
                                                    ).one_or_none()

        if user_to_delete is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

        session.delete(user_to_delete)
        session.commit()
        return Response(status_code=HTTP_204_NO_CONTENT, content=None)



