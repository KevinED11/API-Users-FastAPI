from main import User
from requests import *
from typing import List, Dict


class TestClass:
    def test_read_root(self):
        response = get("http://localhost:8000/")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == {"message": "Welcome to my API"}

    def test_get_users(self):
        response = get("http://localhost:8000/users")
        assert response.status_code == 200
        users_response: List[Dict] = response.json()
        users_list_obj: List[User] = [User(**user) for user in users_response]
        assert all(isinstance(i, User) for i in users_list_obj)
        print(users_list_obj)

    def test_create_user(self):
        response = post("http://localhost/users")
        assert  response.status_code == 200
        new_user = response.json()
        assert new_user['id'] in new_user and new_user['username'] and new_user['password'] and new_user['age']
        print(new_user)

    def test_get_user_by_id(self):
        pass

    def test_delete_user(self):
        pass

