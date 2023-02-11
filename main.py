from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from config.init_db import create_db_and_table
from routes.users.root_get import rootGet
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
    create_db_and_table()


app.include_router(rootGet)


app.include_router(infoGet)


app.include_router(userCreation)


app.include_router(usersGet)


app.include_router(userFind)



app.include_router(userDelete)


app.include_router(userUpdate)


app.include_router(userUpdateField)