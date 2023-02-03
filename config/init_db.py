from models.User_Db import NewUser
from config.db_connection import engine
from sqlmodel import SQLModel, Session


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def create_new_users():

    session = Session(engine)
    session.commit()

def main():
    create_db_and_table()
    create_new_users()

if __name__ == '__main__':
    main()