from fastapi import FastAPI

# uvicorn server
from uvicorn import run as uvicorn_run
# chargue env variables in app
from dotenv import load_dotenv

load_dotenv()

# init db
from backend.config.init_db import add_tables_in_db
# static file server
from starlette.staticfiles import StaticFiles
# middleware
from starlette.middleware.gzip import GZipMiddleware

# routes
from backend.routes.ui_client.root import getAppFrontend
from backend.routes.users.info import infoGet
from backend.routes.users.create import userCreation
from backend.routes.users.get_all import usersGet
from backend.routes.users.find_by_uuid import findByUuid
from backend.routes.users.find_by_id import findById
from backend.routes.users.update import userUpdate
from backend.routes.users.delete import userDelete
from backend.routes.users.update_field import userUpdateField
from backend.routes.users.filter_users import filterUsers

app = FastAPI()


@app.on_event("startup")
def on_startup():
    add_tables_in_db()


# middlewares
app.add_middleware(GZipMiddleware, minimum_size=400)

# static files server
app.mount("/assets/", StaticFiles(directory="frontend/dist/assets"), name="assets")

# send main html file to frontend
app.include_router(getAppFrontend)

app.include_router(infoGet)

app.include_router(userCreation)

app.include_router(usersGet)

app.include_router(filterUsers)

app.include_router(findByUuid)

app.include_router(findById)

app.include_router(userDelete)

app.include_router(userUpdate)

app.include_router(userUpdateField)

if __name__ == "__main__":
    uvicorn_run(app=app, host="0.0.0.0", port=8000)
