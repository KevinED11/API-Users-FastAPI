from sqlmodel import create_engine
from os import getenv
from sqlalchemy.engine import Engine

database_url: str = getenv("DATABASE_URL")
engine: Engine = create_engine(url=database_url, echo=True)


