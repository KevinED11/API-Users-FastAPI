from sqlmodel import SQLModel, Session
from backend.models.database.Users import Users
from backend.config.db_connection import engine
def add_tables_in_db():
  SQLModel.metadata.create_all(engine)

def save_table_in_db():
    with Session(engine) as session:
        session.commit()

def main():
    add_tables_in_db()
    save_table_in_db()

if __name__ == '__main__':
    main()