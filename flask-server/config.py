from os import getenv
from dotenv import load_dotenv

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQLALCHEMY_DB_URI = getenv('SQLALCHEMY_DB_URI')

# engine = create_engine(SQLALCHEMY_DB_URI, future=True, pool_pre_ping=True)
# Base = declarative_base()