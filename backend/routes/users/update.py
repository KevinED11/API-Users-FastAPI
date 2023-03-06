from fastapi import APIRouter, HTTPException, Body
from backend.config.db_connection import engine
from backend.models.update.UpdateUser import UpdateUser
from backend.models.read.UserRead import UserRead
from backend.models.database.Users import Users
from sqlmodel import Session, select
from uuid import UUID
from backend.exceptions.exception_handlers import raise_404_not_found
from starlette.status import HTTP_200_OK
from backend.Password import Password

update_user = APIRouter(tags=['Users'])


@update_user.put('/users/{user_id}', response_model=UserRead, status_code=HTTP_200_OK, response_description='Updated user exist')
async def user_update(user_id: UUID, updated_user: UpdateUser = Body(
    example={
        "name": "Jon",
        "surname": "Gomez",
        "username": "GOMEZ",
        "age": 25,
        "email": "Jhon@gomez.com",
        "password": "PASSWORD",
    }
)) -> Users:
    with Session(engine) as session:
        existing_user_to_update: Users | None = session.exec(select(Users)
                                                             .where((Users.id_user == user_id))
                                                             ).first()

        if existing_user_to_update is None:
            raise_404_not_found(detail="User not found")

        (existing_user_to_update.name,
         existing_user_to_update.surname,
         existing_user_to_update.username,
         existing_user_to_update.age,
         existing_user_to_update.email,
         existing_user_to_update.password) = (
            updated_user.name,
            updated_user.surname,
            updated_user.username,
            updated_user.age,
            updated_user.email,
            Password.encrypt_password(updated_user.password)
            if not Password.verify_password(password=updated_user.password,
                                            hashed_password=existing_user_to_update.password)
            else existing_user_to_update.password
        )

        session.commit()
        session.refresh(existing_user_to_update)

        return existing_user_to_update
