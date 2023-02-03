from sqlmodel import create_engine
import os
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")

