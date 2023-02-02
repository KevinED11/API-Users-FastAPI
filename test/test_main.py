from models.User import User
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

    def test_create_user(self):
        header = {'Accept': 'application/json'}
        response = post("http://localhost/users", headers=header)
        assert  response.status_code == 200
        new_user = response.json()
        assert new_user['id'] in new_user and new_user['username'] and new_user['password'] and new_user['age']
        print(new_user)

    def test_get_user_by_id(self):
        random_id = uuid4()
        response = get(f"http://localhost:8000/users/{random_id}")
        assert response.status_code == 404, 'User not found'
        assert response.status_code == 200
        user_response_dict: Dict = response.json()
        print(user_response_dict)
        obj_user: User = User(**user_response_dict)
        assert isinstance(obj_user, User)



    def test_delete_user(self):
        pass

