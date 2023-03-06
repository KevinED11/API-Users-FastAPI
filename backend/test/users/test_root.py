from requests import get, RequestException
from starlette.responses import Response
from starlette.status import HTTP_200_OK


def test_index_app() -> None | RequestException:
    try:
        response: Response = get("http://localhost:8000/")
        assert response.status_code == HTTP_200_OK
        assert isinstance(response.content, bytes)
        assert response.headers["content-type"] == "text/html; charset=utf-8"
    except RequestException as error:
        return error
