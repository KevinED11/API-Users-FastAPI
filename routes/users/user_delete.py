from routes.users.user_find import *
from fastapi import Response

userDelete = APIRouter()

@userDelete.delete('/users/{user_id}', response_model = None, status_code=204, response_description='User deleted')
async def delete_user(user_id: UUID):
    if user_id in users_id_dict:
        user = users_id_dict.pop(user_id)
        users_ls.remove(user)
        return Response(status_code=204, content=None)
    raise HTTPException(status_code=404, detail='User not found')
