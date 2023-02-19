from fastapi import APIRouter, HTTPException
from config.db_connection import engine
from sqlmodel import Session, select
from models.database.Users import Users as UsersInTable
from models.read.UserRead import UserRead
from models.database.Users import Users
from models.update.UpdateFields import UpdateFields
from uuid import UUID
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from Password import Password
userUpdateField = APIRouter(tags=['Users'])

@userUpdateField.patch('/users/{user_uuid}', response_model=UserRead, status_code=HTTP_200_OK)
async def field_update(user_uuid: UUID, new_data: UpdateFields) -> Users:
    with Session(engine) as session:
        existing_user_to_update: Users | None = session.exec(select(UsersInTable)
                                                             .where( (user_uuid == UsersInTable.id_user) )
                                                             ).one_or_none()

        if not existing_user_to_update:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

        new_data.password = (Password.encrypt_password(new_data.password)
                             if not Password.verify_password(new_data.password, existing_user_to_update.password)
                             else existing_user_to_update.password)

        for (key, value) in new_data.dict(exclude_unset=True).items():
            setattr(existing_user_to_update, key, value)

        session.commit()
        session.refresh(existing_user_to_update)
        return existing_user_to_update





