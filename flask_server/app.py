from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from config import Config
from views import home_page, auth
from models import db
from views import bcrypt, server_session

app = Flask(__name__)
app.config.from_object(Config)

# db = SQLAlchemy(app)
db.init_app(app)
bcrypt.init_app(app)
server_session.init_app(app)


with app.app_context():
    db.create_all()
    db.session.commit()


app.register_blueprint(home_page)
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)