from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Response, Body
from sqlmodel import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from backend.Password import Password
from backend.config.db_connection import engine
from backend.models.database.Users import Users
from backend.models.read.UserRead import UserRead
from backend.models.request.UserCreation import UserCreation

userCreation = APIRouter(tags=['Users'])


@userCreation.post('/users', response_model=UserRead,
                   status_code=HTTP_200_OK,
                   response_description='Created a new user')
async def create_user(user_request: UserCreation = Body(example={
  "name": "Jhon",
  "surname": "Gomez",
  "username": "JGOMEZ",
  "age": 25,
  "email": "Jhon@gomez.com",
  "password": "PASSWORD",
}
)) -> Response:
    user_request.id_user = uuid4()
    user_request.created_at = datetime.now()

    user_request.password = Password.encrypt_password(user_request.password)

    with Session(engine) as session:
        new_user = Users(**user_request.dict())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        #session.add(Users.from_orm(user_request))
        #session.commit()

    return Response(status_code=HTTP_201_CREATED, 
                    content=str({'message': 'user created successfully', 'user_id': user_request.id_user,
                                 'username': user_request.username})
                    )
