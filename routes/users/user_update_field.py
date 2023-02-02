from routes.users.user_creation import *

userUpdateField = APIRouter()

@userUpdateField.patch('/users/{user_id}', response_model=None, status_code=200)
async def field_update(user_id: UUID, name: Optional[str] = None, surname: Optional[str] = None, email: Optional[str] = None ):
    pass