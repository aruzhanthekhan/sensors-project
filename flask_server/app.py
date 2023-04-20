from flask import Flask
from flask_cors import CORS
from config import Config
from views import home_page, auth, user, building
from models import db, migrate, ma
from views import bcrypt, server_session, login_manager, jwt
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
server_session.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
jwt.init_app(app)

app.config["JWT_SECRET_KEY"] = "H2tS80zvIg4VY0g"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)


CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})


with app.app_context():
    db.create_all()
    db.session.commit()


app.register_blueprint(home_page)
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(building)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)