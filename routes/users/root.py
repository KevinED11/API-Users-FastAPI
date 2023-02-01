from fastapi import APIRouter

app_root = APIRouter()


@app_root.get("/", status_code=200)
async def read_root():
    return {"message": "Welcome to my API"}
