from routes.users.user_delete import *
from Password import Password

userCreation = APIRouter()

@userCreation.post('/users', response_model = User, status_code=201, response_description='Created a new user')
async def create_user(user_obj: User):
    user_obj.id = uuid4()
    user_obj.created_at = datetime.now()
    user_obj.password = Password.encrypt_password(Password.gen_password())

    if user_obj.age < 18:
        raise HTTPException(status_code=400, detail='User is under age(place number >= 18)')

    for existing_user in users_ls:
        if user_obj.email == existing_user.email and user_obj.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with email ({user_obj.email}) and username ({user_obj.username}) already exists')
        elif user_obj.username == existing_user.username:
            raise HTTPException(status_code=400, detail=f'User with Username ({user_obj.username}) already exists')
        elif user_obj.email == existing_user.email:
            raise HTTPException(status_code=400, detail=f' User with email ({user_obj.email}) already exists')

    users_ls.append(user_obj)
    users_id_dict[user_obj.id] = user_obj
    return Response(status_code=201, content=str({'message': 'user created successfully', 'user_id': user_obj.id, 'username': user_obj.name}))