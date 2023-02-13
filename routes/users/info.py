from fastapi import APIRouter, Depends
from config.settings import Settings
from functools import lru_cache
from dotenv import get_key

infoGet = APIRouter(tags=['Default'])

@lru_cache()
def get_settings():
    return Settings()

@infoGet.get('/info', response_model = dict[str, str], status_code = 200, response_description='The information was obtained successfully')
async def info_get(settings: Settings = Depends(get_settings)):
    return {
        "app_name": get_key(settings.Config.env_file, 'APP_NAME'),
        "admin_email": get_key(settings.Config.env_file, 'ADMIN_EMAIL')
    }
