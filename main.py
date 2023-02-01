from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List, Dict
from uuid import uuid4, UUID
from datetime import datetime
from password import gen_password, encrypt_password
from routes.users.root import app_root

app = FastAPI()

class User(BaseModel):
    id: UUID
    name: str
    surname: str
    username: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime

    #@validator("age")
    #def validate_age(cls, age):
     #   if age < 18:
      #      raise HTTPException(status_code=400, detail="Place age more than 18 characters")
    #@validator("password")
    #def validate_password(cls, v):
     #   if len(v) < 12:
      #      raise ValueError('Place 12 or more characters')
       # return v


users_ls: List[User] = [


]

users_id_dict: Dict[UUID, User] = {


}


app.include_router(app_root)

@app.get('/users', response_model = List[User])
async def get_users(name: Optional[str] = None, age: Optional[int] = None):
    filtered_users = users_ls

    if name and age:
        filtered_users = [user for user in filtered_users if user.name == name and user.age == age]
    elif name:
        filtered_users = [user for user in filtered_users if user.name == name]
    elif age:
        filtered_users = [user for user in filtered_users if user.age == age]

    return filtered_users

@app.post('/users', response_model = User, status_code=201, response_description='Created a new user')
async def create_user(user: User):
    user.id = uuid4()
    user.created_at = datetime.now()
    user.password = encrypt_password(gen_password())

    #if user.age < 18:
        #raise HTTPException(status_code=400, detail='User is under age(place number >= 18)')

    for existing_user in users_ls:
        if user.email == existing_user.email and user.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with email ({user.email}) and username ({user.username}) already exists')
        elif user.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with Username ({user.username}) already exists')
        elif user.email == existing_user.email:
            raise HTTPException(status_code=400, detail=f' User with email ({user.email}) already exists')

    users_ls.append(user)
    users_id_dict[user.id] = user
    return Response(status_code=201, content=str({'message': 'user created successfully', 'user_id': user.id, 'username': user.name}))

@app.get('/users/{user_id}', response_model = User, response_description='User found')
async def get_user_by_id(user_id: UUID):
    if user_id in users_id_dict:
        return users_id_dict[user_id]
    else:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

@app.delete('/users/{user_id}', response_model = None, status_code=204, response_description='User deleted')
async def delete_user(user_id: UUID):
    if user_id in users_id_dict:
        user = users_id_dict.pop(user_id)
        users_ls.remove(user)
        return Response(status_code=204, content=None)
    raise HTTPException(status_code=404, detail='User not found')


@app.put('/users/{user_id}', response_model= User,  status_code=200, response_description='Updated user')
async def update_user(user_id: UUID, updated_user: User):
    if user_id not in users_id_dict:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

    user: User = users_id_dict[user_id]

    user.username, user.name, user.email, user.surname, user.age = (
        updated_user.username,
        updated_user.name,
        updated_user.email,
        updated_user.surname,
        updated_user.age
    )
    #user.username = updated_user.username
    #user.name = updated_user.name
    #user.email = updated_user.email
    #user.surname = updated_user.surname
    #user.age = updated_user.age

    users_id_dict[user_id] = user

    for i, existing_user in enumerate(users_ls):
        if existing_user.id == user_id:
            users_ls[i] = user

    return user



