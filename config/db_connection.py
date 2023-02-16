from sqlmodel import create_engine
from os import getenv

database_url = getenv('DATABASE_URL')
engine = create_engine(url=database_url, echo=True)
