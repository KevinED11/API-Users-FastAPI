from fastapi import APIRouter
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from fastapi import HTTPException
from models.request.UserCreation import UserCreation
from uuid import UUID
from starlette.responses import HTMLResponse, JSONResponse
users_ls: list[UserCreation] = [


]

users_id_dict:dict[UUID | UserCreation] = {


}

getAppFrontend = APIRouter(tags=['Frontend'])


@getAppFrontend.get("/", status_code=200,
    responses={
    HTTP_200_OK: {"description": "Successful response"},
    HTTP_404_NOT_FOUND: {"description": "File not found"}
})
async def get_app_frontend():

    try:
        with open("./frontend/dist/index.html", "r") as app_react:
            content_app = app_react.read()
        return HTMLResponse(content=content_app, status_code=200)


    except FileNotFoundError:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="File not found")
        #return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"description": "File not found"})

