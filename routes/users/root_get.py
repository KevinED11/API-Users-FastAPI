from fastapi import APIRouter
from typing import List, Dict
from models.User import User
from uuid import UUID

users_ls: List[User] = [


]

users_id_dict: Dict[UUID, User] = {


}

rootGet = APIRouter()



@rootGet.get("/", status_code=200)
async def read_root():
    return {"message": "Welcome to my API"}


