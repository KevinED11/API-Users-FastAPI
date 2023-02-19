from fastapi import APIRouter, Depends
from config.settings import Settings
from functools import lru_cache

infoGet = APIRouter(tags=['Admin'])

@lru_cache()
def get_settings():
    return Settings()

@infoGet.get('/info', response_model=dict[str, str], status_code=200, response_description='The information was obtained successfully')
async def info_get(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
