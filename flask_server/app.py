from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import SQLALCHEMY_DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)