from fastapi import APIRouter, Response
from backend.config.db_connection import engine
from sqlmodel import Session, select
from backend.models.database.Users import Users
from uuid import UUID
from backend.exceptions.exception_handlers import raise_404_not_found
from starlette.status import HTTP_204_NO_CONTENT

user_delete = APIRouter(tags=['Users'])


@user_delete.delete('/users/{user_uuid}', response_model=None, status_code=204, response_description='User deleted')
async def delete_user(user_uuid: UUID) -> Response:
    with Session(engine) as session:

        user_to_delete: Users | None = session.exec(select(Users)
                                                    .where((user_uuid == Users.id_user))
                                                    ).one_or_none()

        if user_to_delete is None:
            raise_404_not_found(detail="User not found")

        session.delete(user_to_delete)
        session.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)
