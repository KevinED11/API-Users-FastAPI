from pydantic import BaseSettings, Field
from typing import Optional
from os import getenv


class Settings(BaseSettings):
    app_name: Optional[str] = Field(default=getenv("APP_NAME"))
    admin_email: Optional[str] = Field(default=getenv("ADMIN_EMAIL"))

    class Config:
        env_file: str = ".env"
