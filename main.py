from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr
from uuid import uuid4, UUID
from datetime import datetime
from string import ascii_letters, digits, punctuation
from secrets import choice

app = FastAPI()

class User(BaseModel):
    id: UUID
    name: str
    surname: str
    age: int
    email: EmailStr
    password: str
    created_at: datetime


users = [


]


@app.get("/")
async def read_root():
    return 'Welcome to mi API'


@app.get('/users')
async def get_users():
    return users


@app.post('/users')
async def create_user(user: User):
    user.id = uuid4()
    user.created_at = datetime.now()
    user.password == ''.join(choice(ascii_letters + digits + punctuation) for i in range(10))

    if user.age < 18:
        raise HTTPException(status_code=400, detail='User is under age')

    for existing_user in users:
        if user.email == existing_user.email or user.name == existing_user.name:
            raise HTTPException(status_code=400, detail='User already exists')
    users.append(user)
    return users[-1]


@app.get('/users/{user_id}')
async def get_user_by_id(user_id: UUID):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/users/{user_id}')
async def delete_user(user_id: UUID):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return Response(content=None, status_code=204)
    raise HTTPException(status_code=404, detail='User not found')


