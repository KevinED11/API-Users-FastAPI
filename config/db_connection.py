from sqlmodel import create_engine
from dotenv import get_key
from config.settings import Settings
import os


database_url = get_key(dotenv_path=Settings.Config.env_file, key_to_get='DATABASE_URL')
database = os.getenv('DATABASE_URL')


engine = create_engine(database, echo=True)
