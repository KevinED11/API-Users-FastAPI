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
from backend.middlewares.middlewares import gzip_middleware, cors_middleware
# routes
from backend.routes.client.root import frontend_app
from backend.routes.users.info import admin_info
from backend.routes.users.create import user_creation
from backend.routes.users.get_all import users_get
from backend.routes.users.find_by_uuid import find_by_uuid
from backend.routes.users.find_by_id import find_by_id
from backend.routes.users.update import update_user
from backend.routes.users.delete import user_delete
from backend.routes.users.update_field import user_update_fields
from backend.routes.users.filter_users import search_users

app = FastAPI()


@app.on_event("startup")
def on_startup():
    add_tables_in_db()


# middlewares
app.add_middleware(middleware_class=gzip_middleware, minimum_size=300)
app.add_middleware(middleware_class=cors_middleware, allow_origins=["*"],
                   allow_methods=["get"],
                   )
# static files server
app.mount("/assets/", StaticFiles(directory="frontend/dist/assets"), name="assets")

# send main html
app.include_router(frontend_app)

# routes for users
app.include_router(admin_info)

app.include_router(user_creation)

app.include_router(users_get)

app.include_router(search_users)

app.include_router(find_by_uuid)

app.include_router(find_by_id)

app.include_router(user_delete)

app.include_router(update_user)

app.include_router(user_update_fields)
# end routes for users

if __name__ == "__main__":
    uvicorn_run(app=app, host="0.0.0.0", port=8000)
