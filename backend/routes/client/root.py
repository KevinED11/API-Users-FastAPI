from fastapi import APIRouter, Depends
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from fastapi import HTTPException
from starlette.responses import HTMLResponse
from functools import lru_cache

frontend_app = APIRouter(tags=['Frontend'])


@lru_cache()
def read_index() -> str:
    try:
        with open("frontend/dist/index.html", "r") as app_react:
            content_app: str = app_react.read()
        return content_app

    except FileNotFoundError:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="File not found")


@frontend_app.get("/", status_code=HTTP_200_OK, responses={
                        HTTP_200_OK: {"description": "Successful response"},
                        HTTP_404_NOT_FOUND: {"description": "File not found"}
                    })
async def get_frontend(app_react: str = Depends(read_index)) -> HTMLResponse:
    return HTMLResponse(content=app_react, status_code=HTTP_200_OK, media_type="text/html",
                        headers={"Cache-Control": "max-age=3600"})
