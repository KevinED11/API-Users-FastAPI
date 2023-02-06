from config.db_connection import engine
from sqlmodel import SQLModel, Session


def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def save_table_in_db():
    session = Session(engine)
    session.commit()
    session.close()

def main():
    create_db_and_table()
    save_table_in_db()

if __name__ == '__main__':
    main()