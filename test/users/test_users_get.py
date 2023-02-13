from requests import get, RequestException
from models.request.UserCreation import UserCreation
def test_get_users():
    try:
        response = get("http://127.0.0.1:8000/users")
        print(f'server response: {response.json()}')
        print(f'contenido respuesta: {response.content}')

        assert response.status_code == 200
        users_response_dict: list[dict] = response.json()
        users_list_obj: list[UserCreation] = [UserCreation(**user) for user in users_response_dict]
        assert all(isinstance(i, UserCreation) for i in users_list_obj)
        print(f'json a obj User: {users_list_obj}')
    except RequestException as error:
        return error
