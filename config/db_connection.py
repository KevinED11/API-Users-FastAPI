from sqlmodel import create_engine
from dotenv import get_key
from config.settings import Settings

database_url = get_key(dotenv_path=Settings.Config.env_file, key_to_get='DATABASE_URL')
engine = create_engine(database_url, echo=True)

