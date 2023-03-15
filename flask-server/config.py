from os import getenv
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DB_URI = getenv('SQLALCHEMY_DB_URI')