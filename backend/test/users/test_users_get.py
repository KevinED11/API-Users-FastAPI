from requests import get, RequestException
from models.request.UserCreation import UserCreation
from starlette.status import HTTP_200_OK

def test_get_users() -> list[UserCreation | None] | RequestException:
    try:
        response = get("http://127.0.0.1:8000/users")
        #verify status code == 200
        assert response.status_code == HTTP_200_OK
        #convert response in list with dictionary
        response_list_user: list[dict] = response.json()
        #verify response_list_user variable is instance of list
        assert isinstance(response_list_user, list)
        #verify length response_list_user variable is > 0
        assert len(response_list_user) > 0
        #create list of object types User-creation from response_list_user
        users_list_obj: list[UserCreation] = list(UserCreation(**user) for user in response_list_user)
        #verify for each item in users_list_obj == instance of User-creation
        assert all(isinstance(i, UserCreation) for i in users_list_obj)
    except RequestException as error:
        return error

