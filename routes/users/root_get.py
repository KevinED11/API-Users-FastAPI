from fastapi import APIRouter
rootGet = APIRouter()


@rootGet.get("/", status_code=200)
async def read_root():
    return {"message": "Welcome to my API"}
