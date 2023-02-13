from fastapi import APIRouter, HTTPException, Body
from config.db_connection import engine
from models.request.UserCreation import UserCreation
from models.database.Users import Users
from sqlmodel import Session, select
from uuid import UUID
from routes.frontend.app import users_id_dict, users_ls



userUpdate = APIRouter(tags=['Users'])


@userUpdate.put('/users/{user_id}', response_model= UserCreation, status_code=200, response_description='Updated user exist')
async def update_user(user_id: UUID, updated_user: UserCreation = Body(
    example= {
  "name": "Jhon",
  "surname": "Gomez",
  "username": "JGOMEZ",
  "age": 25,
  "email": "Jhon@gomez.com",
  "password": "PASSWORD",
}
)):
    with Session(engine) as session:
        users_all = session.exec(select(Users)).all()

        for user_db in users_all:
            if user_db.id_user == user_id:
                user_exist: Users = user_db

        user_exist.username, user_exist.name, user_exist.email, user_exist.surname, user_exist.age = (
            updated_user.username,
            updated_user.name,
            updated_user.email,
            updated_user.surname,
            updated_user.age
        )

        for i, existing_user in enumerate(users_all):
            if existing_user.id_user == user_id:
                users_all[i] = user_exist

        session.commit()
        session.refresh(user_exist)
        return user_exist








    if user_id not in users_id_dict:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

    user_exist: UserCreation = users_id_dict[user_id]

    user_exist.username, user_exist.name, user_exist.email, user_exist.surname, user_exist.age = (
        updated_user.username,
        updated_user.name,
        updated_user.email,
        updated_user.surname,
        updated_user.age
    )

    users_id_dict[user_id] = user_exist

    for i, existing_user in enumerate(users_ls):
        if existing_user.id_user == user_id:
            users_ls[i] = user_exist

    return user_exist