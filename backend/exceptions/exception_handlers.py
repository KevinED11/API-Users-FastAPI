from fastapi.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


def raise_404_not_found(detail: str) -> None:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=detail)


