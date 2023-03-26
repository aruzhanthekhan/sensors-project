from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from views import home_page

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


from models import User, Admin, Chairman, Building, chairmenBuildings


with app.app_context():
    db.create_all()
    db.session.commit()


app.register_blueprint(home_page)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)