from fastapi import APIRouter, HTTPException, Query
from models.database.Users import Users
from models.read.UserRead import UserRead
from config.db_connection import engine
from sqlmodel import Session, select
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from typing import Optional
filterUsers = APIRouter(tags=["Users"])

@filterUsers.get("/users/filter", response_model=list[UserRead], status_code=HTTP_200_OK)
async def filter_user(name: Optional[str] = None, age: Optional[int] = None):
    with Session(engine) as session:
       pass

    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Users not found")







