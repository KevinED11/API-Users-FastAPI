from fastapi import APIRouter, HTTPException, Response, Body
from models.request.User import User
from datetime import datetime
from Password import Password
from uuid import uuid4
from config.db_connection import engine
from sqlmodel import Session
from models.database.Users import Users

userCreation = APIRouter(tags=['Users'])

@userCreation.post('/users', response_model = User, status_code=201, response_description='Created a new user')
async def create_user(user_request: User = Body(example=
{
  "name": "Jhon",
  "surname": "Gomez",
  "username": "JGOMEZ",
  "age": 25,
  "email": "Jhon@gomez.com",
  "password": "PASSWORD",
}
)):
    user_request.id_user = uuid4()
    user_request.created_at = datetime.now()
    user_request.password = Password.encrypt_password(Password.gen_password())

    if user_request.age < 18:
        raise HTTPException(status_code=400, detail='User is under age(place number >= 18)')

    with Session(engine) as session:
        new_user = Users(**user_request.dict())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        #session.add(Users.from_orm(user_request))
        #session.commit()

    return Response(status_code=201, content=str({'message': 'user created successfully', 'user_id': user_request.id_user, 'username': user_request.username}))

