from fastapi import FastAPI
from routes.users.root_get import rootGet
from routes.users.user_creation import userCreation
from routes.users.users_get import usersGet
from routes.users.user_find import userFind
from routes.users.user_update import userUpdate
from routes.users.user_delete import userDelete
from routes.users.user_update_field import userUpdateField



app = FastAPI()





app.include_router(rootGet)


app.include_router(userCreation)


app.include_router(usersGet)


app.include_router(userFind)



app.include_router(userDelete)


app.include_router(userUpdate)


app.include_router(userUpdateField)