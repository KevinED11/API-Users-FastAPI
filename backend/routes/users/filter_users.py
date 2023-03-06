from fastapi import APIRouter
from backend.models.database.Users import Users
from backend.models.read.UserRead import UserRead
from backend.config.db_connection import engine
from sqlmodel import Session, select, and_
from backend.exceptions.exception_handlers import raise_404_not_found
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from starlette.responses import Response
from typing import Optional

search_users = APIRouter(tags=["Users"])


@search_users.get("/users/search", response_model=list[UserRead], status_code=HTTP_200_OK)
async def filter_user(name: Optional[str] = None, age: Optional[int] = None) -> list[Users] | Response:
    with Session(engine) as session:
        # return users list o user

        if name is None and age is None:
            return Response(status_code=HTTP_204_NO_CONTENT)

        users_filter: list[Users] | list = session.exec(select(Users)
                                                        .where(and_((name is None or Users.name == name),
                                                                    (age is None or Users.age == age)))
                                                        ).all()
        if users_filter:
            return users_filter

        raise_404_not_found(detail="User not found, no coincidence with placed params")
