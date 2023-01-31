from fastapi import APIRouter
from main import *

auth_router = APIRouter()

@auth_router.post('/login')
async def login(username: str, password: str):
    pass



app.include_router(auth_router)
