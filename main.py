from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr, Required
from typing import Optional, List, Dict
from uuid import uuid4, UUID
from datetime import datetime
from password import gen_password, encrypt_password

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


users: List[User] = [


]

users_id_dict: Dict[UUID, User] = {


}

@app.get("/")
async def read_root():
    return {"message": "Welcome to my API"}

@app.get('/users', response_model = List[User])
async def get_users(name: Optional[str] = None, age: Optional[int] = None):
    filtered_users = users

    if name and age:
        filtered_users = [user for user in filtered_users if user.name == name and user.age == age]
    elif name:
        filtered_users = [user for user in filtered_users if user.name == name]
    elif age:
        filtered_users = [user for user in filtered_users if user.age == age]

    return filtered_users

@app.post('/users', response_model = Dict)
async def create_user(user: User):
    user.id = uuid4()
    user.created_at = datetime.now()
    user.password = encrypt_password(gen_password())

    if user.age < 18:
        raise HTTPException(status_code=400, detail='User is under age(place number >= 18)')

    for existing_user in users:
        if user.email == existing_user.email and user.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with email ({user.email}) and username ({user.username}) already exists')
        elif user.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with Username ({user.username}) already exists')
        elif user.email == existing_user.email:
            raise HTTPException(status_code=400, detail=f' User with email ({user.email}) already exists')

    users.append(user)
    users_id_dict[user.id] = user
    return Response(status_code=201, content=str({'message': 'user created successfully', 'user_id': user.id, 'username': user.name}))

@app.get('/users/{user_id}', response_model = User)
async def get_user_by_id(user_id: UUID):
    if user_id in users_id_dict:
        return users_id_dict[user_id]
    else:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

    #for user in users:
        #if user.id == user_id:
            #return user
    #raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

@app.delete('/users/{user_id}', response_model = None)
async def delete_user(user_id: UUID):
    if user_id in users_id_dict:
        user = users_id_dict.pop(user_id)
        users.remove(user)
        return Response(status_code=204, content=None)
    raise HTTPException(status_code=404, detail='User not found')

    #for i, user in enumerate(users):
        #if user.id == user_id:
            #users.pop(i)
            #return Response(content=None, status_code=204)
    #raise HTTPException(status_code=404, detail='User not found')

@app.put('users/{user_id}')
async def update_user():
    pass

