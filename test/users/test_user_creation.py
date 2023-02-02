from requests import post, RequestException
from models.User import User
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
        print(f'la respuesta fue: {response.content}')
        assert response.status_code == 201
        new_user = response.json()
        dict_to_user = User(**new_user)
        assert isinstance(dict_to_user, User)
        print(dict_to_user)
    except RequestException as error:
        return error