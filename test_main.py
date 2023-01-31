from main import User
from requests import *
from typing import List, Dict
from uuid import UUID, uuid4

class TestClass:
    def test_read_root(self):
        response = get("http://localhost:8000/")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == {"message": "Welcome to my API"}

    def test_get_users(self):

        response = get("http://localhost:8000/users")
        print(f'server response: {response.json()}')
        print(f'contenido respuesta: {response.content}')

        assert response.status_code == 200
        users_response_dict: List[Dict] = response.json()
        users_list_obj: List[User] = [User(**user) for user in users_response_dict]
        assert all(isinstance(i, User) for i in users_list_obj)
        print(f'json a obj User: {users_list_obj}')





    def test_delete_user(self):
        pass

