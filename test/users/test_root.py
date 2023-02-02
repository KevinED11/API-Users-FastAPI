from requests import get, RequestException
def test_read_root():
    try:
        response = get("http://localhost:8000/")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == {"message": "Welcome to my API"}
    except RequestException as error:
        return error