from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: Optional[str]
    admin_email: Optional[str]

    class Config:
        env_file: str = '.env'


