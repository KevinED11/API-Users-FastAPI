from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from uuid import uuid4, UUID
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    id: UUID
    name: str
    surname: str
    email: EmailStr
    age: int
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



#Falta agregar put y delete