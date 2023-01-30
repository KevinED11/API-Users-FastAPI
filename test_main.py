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



