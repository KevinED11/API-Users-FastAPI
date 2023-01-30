from requests import *
from typing import Dict
class TestClass:
    def test_read_root(self):
        response = get("http://localhost:8000/")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == {"message": "Welcome to my API"}


    def test_get_users(self):
        response = get("http://localhost/users")
        assert response.status_code == 200
        users = response.json()
        assert all(isinstance(i, Dict) for i in users)
        print(users)
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

