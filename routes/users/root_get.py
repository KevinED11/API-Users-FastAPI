from fastapi import APIRouter
from models.request.User import User
from uuid import UUID


users_ls: list[User] = [


]

users_id_dict:dict[UUID | User] = {


}

rootGet = APIRouter(tags=['Default'])



@rootGet.get("/", status_code=200)
async def read_root():
    return {"message": "Welcome to my API"}


