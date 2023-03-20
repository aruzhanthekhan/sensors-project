from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)