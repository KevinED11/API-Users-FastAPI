from routes.users.user_creation import *


userUpdate = APIRouter()


@userUpdate.put('/users/{user_id}', response_model= User, status_code=200, response_description='Updated user')
async def update_user(user_id: UUID, updated_user: User):
    if user_id not in users_id_dict:
        raise HTTPException(status_code=404, detail=f'User with id {user_id} not found')

    user: User = users_id_dict[user_id]

    user.username, user.name, user.email, user.surname, user.age = (
        updated_user.username,
        updated_user.name,
        updated_user.email,
        updated_user.surname,
        updated_user.age
    )

    users_id_dict[user_id] = user

    for i, existing_user in enumerate(users_ls):
        if existing_user.id == user_id:
            users_ls[i] = user

    return user