from sqlmodel import SQLModel, Session
import models.database
from config.db_connection import engine
def add_tables_in_db():
  SQLModel.metadata.create_all(bind=engine)

def save_table_in_db():
    with Session(bind=engine) as session:
        session.commit()

def main():
    add_tables_in_db()
    save_table_in_db()

if __name__ == '__main__':
    main()