from os import getenv
from dotenv import load_dotenv

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

db_data = {
    'user': getenv('DB_USERNAME'),
    'password': getenv('DB_PASSWORD'),
    'host': getenv('DB_HOST'),
    'name': getenv('DB_NAME')
}

class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_data["user"]}:{db_data["password"]}@{db_data["host"]}/{db_data["name"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = '/flask_session/'

# engine = create_engine(SQLALCHEMY_DB_URI, future=True, pool_pre_ping=True)
# Base = declarative_base()