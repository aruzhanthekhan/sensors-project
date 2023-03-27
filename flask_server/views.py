from flask import Blueprint, request, session
from flask_bcrypt import Bcrypt
from flask_session import Session

from models import User, Admin, Chairman, Building


bcrypt = Bcrypt()
server_session = Session()


home_page = Blueprint('home', __name__)
auth = Blueprint('auth', __name__)


@home_page.route('/', methods=['GET'])
def home():
    return Building.get_all().serialize_list()


@auth.route('/login', methods=['POST'])
def sign_in():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.get(email=email)

    if user is None:
        return dict(status=401, comment="This user does not exist")
    
    if not bcrypt.check_passwoed_hash(user.password, password):
        return dict(status=401, comment="Password is not matched")
    
    session['email'] = email

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
    
    hashedPassword = bcrypt.generate_password_hash(password)

    user = User(firstname=firstname, lastname=lastname, patronymic=patronymic, phone=phone, email=email, password=hashedPassword)
    user.save()

    session['email'] = email

    return user.serialize()


@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('email')
    return dict(status=200, comment="User log out")