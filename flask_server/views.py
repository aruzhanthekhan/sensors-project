import json
from flask import Blueprint, request, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models import User, Building, Roles


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

    print(request.json)
    # firstname = request.json('first_name')
    # lastname = request.json('last_name')
    # patronymic = request.json('fathers_name')
    # phone = request.json('phone')
    # email = request.json('email')
    # password = request.json('password')

    firstname = request.json['first_name']
    lastname = request.json['last_name']
    patronymic = request.json['fathers_name']
    phone = request.json['phone']
    email = request.json['email']
    password = request.json['password']
    
    # if not firstname:
    # # Handle empty password
    #     return "Please enter a valid name"

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
    current_user_id = current_user.get_id()
    user = User.get(id = current_user_id)

    return user.serialize()


@user.route('/addAdmin/<int:user_id>', methods=['PATCH'])
@login_required
def add_admin(user_id: int):
    current_user_id = current_user.get_id()
    current_user = User.get(id=current_user_id)

    if not current_user.is_admin():
        return dict(status=403, comment="User is not admin")
    
    user = User.get(id=user_id)
    user.role = Roles.Admin
    user.update()

    return dict(status=200, comment="Admin successfully added")


@user.route('/addChairman/<int:user_id>', methods=['PATCH'])
@login_required
def add_chairman(user_id: int):
    current_user_id = current_user.get_id()

    if not User.is_admin(current_user_id):
        return dict(status=403, comment="User is not admin")
    
    user = User.get(id=user_id)
    user.role = Roles.Chairman
    user.update()

    return dict(status=200, comment="Chairman successfully added")


@user.route('/dashboard', methods=['GET'])
@login_required
def show_all_users():
    current_user_id = current_user.get_id()

    if not User.is_admin(current_user_id):
        return dict(status=403, comment="User is not admin")
    
    users = User.get_all()
    
    return User.serialize_list(list=users)


@building.route('/addBuilding', methods=['POST'])
@login_required
def add_building():
    current_user_id = current_user.get_id()

    if not User.is_admin(current_user_id) and not User.is_chairman(current_user_id):
        return dict(status=403, comment="User is not admin or chairman")
    
    
    address = request.form.get('address')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    hotWaterPressure = request.form.get('hotWaterPressure')
    coldWaterPressure = request.form.get('coldWaterPressure')
    hotWaterConsumption = request.form.get('hotWaterConsumption')
    coldWaterConsumption = request.form.get('coldWaterConsumption')
    directFlowTemperature = request.form.get('directFlowTemperature')
    returnFlowTemperature = request.form.get('returnFlowTemperature')
    inputVoltage = request.form.get('inputVoltage')
    inputCurrentStrength = request.form.get('inputCurrentStrength')
    createdBy = current_user_id
    redactedBy = current_user_id

    new_building = Building(address=address, latitude=latitude, longitude=longitude, 
                            hotWaterPressure=hotWaterPressure, coldWaterPressure=coldWaterPressure,
                            hotWaterConsumption=hotWaterConsumption, coldWaterConsumption=coldWaterConsumption,
                            directFlowTemperature=directFlowTemperature, returnFlowTemperature=returnFlowTemperature,
                            inputVoltage=inputVoltage, inputCurrentStrength=inputCurrentStrength,
                            createdBy=createdBy, redactedBy=redactedBy)
    new_building.save()

    return new_building.serialize()


@building.route('/updateBuildingParam/<int:building_id>', methods=['POST'])
@login_required
def update_building_parameter(building_id: int):
    current_user_id = current_user.get_id()

    if not User.is_admin(current_user_id):
        return dict(status=403, comment="User is not admin or chairman")
    
    if not User.is_chairman(current_user_id):
        return dict(status=403, comment="User is not admin or chairman")
    
    building = Building.get(id=building_id)
    
    building.address = request.form.get('address')
    building.latitude = request.form.get('latitude')
    building.longitude = request.form.get('longitude')
    building.hotWaterPressure = request.form.get('hotWaterPressure')
    building.coldWaterPressure = request.form.get('coldWaterPressure')
    building.hotWaterConsumption = request.form.get('hotWaterConsumption')
    building.coldWaterConsumption = request.form.get('coldWaterConsumption')
    building.directFlowTemperature = request.form.get('directFlowTemperature')
    building.returnFlowTemperature = request.form.get('returnFlowTemperature')
    building.inputVoltage = request.form.get('inputVoltage')
    building.inputCurrentStrength = request.form.get('inputCurrentStrength')
    building.redactedBy = current_user_id

    building.update()

    return dict(status=200, comment="Successfully updated")
