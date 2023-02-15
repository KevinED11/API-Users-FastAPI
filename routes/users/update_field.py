from fastapi import APIRouter, HTTPException, Query
from config.db_connection import engine
from sqlmodel import Session, select,update
from models.database.Users import Users as UsersInTable
from models.read.UserRead import UserRead
from models.update.UpdateFields import UpdateFields
from uuid import UUID
from starlette.status import HTTP_404_NOT_FOUND

userUpdateField = APIRouter(tags=['Users'])

@userUpdateField.patch('/users/{user_uuid}', response_model=UserRead, status_code=200)
async def field_update(user_uuid: UUID, new_user_data: UpdateFields):
    with Session(engine) as session:
        existing_user_to_update = session.exec(select(UsersInTable).where(user_uuid == UsersInTable.id_user)).one_or_none()

        if not existing_user_to_update:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

        updated_user = UsersInTable.from_orm(new_user_data)


        session.refresh(updated_user)

        return updated_user