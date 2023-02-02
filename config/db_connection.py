from sqlmodel import create_engine, SQLModel
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres", echo=True)

conn = engine.connect()

meta_data = SQLModel()