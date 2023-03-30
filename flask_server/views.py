import json
from flask import Blueprint, request, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_login import LoginManager, login_user, login_required, logout_user

from models import User, Admin, Chairman, Building


bcrypt = Bcrypt()
server_session = Session()
login_manager = LoginManager()


home_page = Blueprint('home', __name__)
auth = Blueprint('auth', __name__)
user = Blueprint('user', __name__)
building = Blueprint('build', __name__)


@home_page.route('/', methods=['GET'])
def home():
    return json.dumps(Building.get_all())


@login_manager.user_loader
def load_user(user_id: int):
    return User.get(id=user_id)


@auth.route('/login', methods=['POST'])
def sign_in():
    session.pop('user_id', None)

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.get(email=email)

    if user is None:
        return dict(status=401, comment="This user does not exist")
    
    if not bcrypt.check_password_hash(user.password, password):
        return dict(status=401, comment="Password is not matched")
    
    login_user(user)
    session['user_id'] = user.id

    return user.serialize()


@auth.route('/register', methods=['POST'])
def sign_up():
    firstname = request.form.get('first-name')
    lastname = request.form.get('last-name')
    patronymic = request.form.get('fathers-name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password = request.form.get('password')


    userExist = User.get(email=email)
    if userExist is not None:
        return dict(status=409, comment="User with this email already exist")
        
    userExist = User.get(phone=phone)
    if userExist is not None:
        return dict(status=409, comment="User with this phone number already exist")
        
    hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')


    user = User(firstname=firstname, lastname=lastname, patronymic=patronymic, phone=phone, email=email, password=hashedPassword)
    user.save()

    return dict(status=200, comment="User successfully created")
    


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    session.pop('user_id')
    return dict(status=200, comment="User log out")


@user.route('/profile', methods=['GET'])
@login_required
def show_profile():
    pass


@building.route('/addBuilding', methods=['POST'])
@login_required
def add_building():
    pass


@building.route('/updateBuildingParam', methods=['POST'])
@login_required
def update_building_parameter():
    pass
