
from sqlmodel import create_engine
from config.settings import Settings
from dotenv import get_key

database_url = get_key(dotenv_path=Settings.Config.env_file, key_to_get='DATABASE_URL')

engine = create_engine(database_url)
