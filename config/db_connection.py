from sqlmodel import create_engine
from config.settings import Settings
from dotenv import get_key

engine = create_engine(get_key(dotenv_path=Settings.Config.env_file, key_to_get='DATABASE_URL'))