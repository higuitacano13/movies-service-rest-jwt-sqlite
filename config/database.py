import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLITE_FILE_NAME = "../database.sqlite"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, SQLITE_FILE_NAME)}"
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()