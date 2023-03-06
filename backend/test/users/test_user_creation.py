from requests import post, RequestException
from backend.models.request.UserCreation import UserCreation


def test_create_user():
    try:
        header = {'Accept': 'application/json'}
        response = post("http://127.0.0.1:8000/users", headers=header, json={
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "asaell",
            "surname": "string",
            "username": "KevinD",
            "age": 25,
            "email": "kevin@example.com",
            "password": "string",
            "created_at": "2023-02-02T18:07:47.575Z"

        })
        new_user = response.json()
        print(new_user)
        print(response)

        if response.status_code == 400 and 'email' in new_user and 'username' in new_user:
            assert response.status_code == 400
            assert new_user['detail'] == f"User with email ({new_user['email']}) and username ({new_user['username']}) already exists"
        elif response.status_code == 201:
            assert response.status_code == 201
            dict_to_user = UserCreation(**new_user)
            assert isinstance(dict_to_user, UserCreation)
    except RequestException as error:
        return error
