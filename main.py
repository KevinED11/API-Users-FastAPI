from fastapi import FastAPI

from uvicorn import run as uvicorn_run
from dotenv import load_dotenv
load_dotenv()

from config.init_db import add_tables_in_db
from starlette.staticfiles import StaticFiles
from routes.frontend.app import getAppFrontend
from routes.users.info import infoGet
from routes.users.user_creation import userCreation
from routes.users.users_get import usersGet
from routes.users.user_find import userFind
from routes.users.user_update import userUpdate
from routes.users.user_delete import userDelete
from routes.users.user_update_field import userUpdateField

app = FastAPI()

@app.on_event("startup")
def on_startup():
    add_tables_in_db()

#static files server

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="static")


app.include_router(getAppFrontend)


app.include_router(infoGet)


app.include_router(userCreation)


app.include_router(usersGet)


app.include_router(userFind)


app.include_router(userDelete)


app.include_router(userUpdate)


app.include_router(userUpdateField)


if __name__ == "__main__":
    uvicorn_run(app=app, host="localhost", port=8000)