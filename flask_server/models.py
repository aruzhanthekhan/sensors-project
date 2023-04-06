import enum
from sqlalchemy.sql import func
from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


class Roles(int, enum.Enum):
    User = 0
    Admin = 1
    Chairman = 2


class BaseClass(object):
    """
    Contains common functions like save and delete
    """
    def save(self):
        db.session.add(self)
        db.session.commit()
    

    def update(self):
        db.session.commit()
    

    def delete(self):
        db.session.delete()
        db.commit()
    

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    

    def serialize_list(list):
        return [m.serialize() for m in list]
    

class User(db.Model, BaseClass, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    patronymic = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), unique=True, nullable=True, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(Roles), nullable=False, default=Roles.User)
    dateOfCreate = db.Column(db.DateTime(timezone=True), server_default=func.now())
    dateOfLastUpdate = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


    def __init__(self, **kwargs):
        keys = ['firstname', 'lastname', 'patronymic', 'phone', 'email', 'password']
        for key in keys:
            setattr(self, key, kwargs.get(key))

    
    @staticmethod
    def get(**kwargs):
        return User.query.filter_by(**kwargs).first()
    

    @staticmethod
    def is_admin(user_id: int) -> bool:
        user = User.get(id=user_id)
        if user.role == 1:
            return True
        
        return False
    

    @staticmethod
    def is_chairman(user_id: int) -> bool:
        user = User.get(id=user_id)
        if user.role == 2:
            return True
        
        return False
    

    @staticmethod
    def get_all():
        return User.query.filter_by().all()

    
class Building(db.Model, BaseClass):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), unique=True, nullable=False)
    latitude = db.Column(db.Numeric(precision=9, scale=7, asdecimal=False, decimal_return_scale=None), unique=True, nullable=False)
    longitude = db.Column(db.Numeric(precision=10, scale=7, asdecimal=False, decimal_return_scale=None), unique=True, nullable=False)
    hot_water_pressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    cold_water_pressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    hot_water_consumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    cold_water_consumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    direct_flow_temperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    return_flow_temperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    input_voltage = db.Column(db.Float, nullable=False, default=0.0, index=True)
    input_current_strength = db.Column(db.Float, nullable=False, default=0.0, index=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=1)
    redacted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=1, onupdate=1)
    date_of_create = db.Column(db.DateTime(timezone=True), server_default=func.now())
    date_of_last_update = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


    def __init__(self, **kwargs):
        keys = ['id', 'address', 'latitude', 'longitude', 'hot_water_pressure', 'cold_water_pressure',
                'hot_water_consumption', 'cold_water_consumption', 'direct_flow_temperature',
                'return_flow_temperature', 'input_voltage', 'input_current_strength']
        
        for key in keys:
            setattr(self, key, kwargs.get(key))


    @staticmethod
    def get(**kwargs):
        return Building.query.filter_by(**kwargs).first()

    
    @staticmethod
    def get_all():
        return Building.query.filter_by().all()


class BuildingSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'address', 'latitude', 'longitude', 'hot_water_pressure', 'cold_water_pressure',
                'hot_water_consumption', 'cold_water_consumption', 'direct_flow_temperature',
                'return_flow_temperature', 'input_voltage', 'input_current_strength')
    
building_schema = BuildingSchema
buildings_schema = BuildingSchema(many=True)


# chairmenBuildings = db.Table('chairmenbuildings',
#     db.Column('chairmanId', db.Integer, db.ForeignKey('chairmen.id')),
#     db.Column('buildingId', db.Integer, db.ForeignKey('buildings.id'))
# )


# class Admin(db.Model, BaseClass):
#     __tablename__ = "admins"

#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

#     buildings = db.relationship('Building', backref='buildings')

#     def __init__(self, **kwargs):
#         keys = ['userId']

#         for key in keys:
#             setattr(self, key, kwargs.get(key))


#     @staticmethod
#     def is_admin(user_id: int):
#         if (Admin.query.filter_by(userId=user_id).first() is not None):
#             return True
        
#         return False


# class Chairman(db.Model, BaseClass):
#     __tablename__ = "chairmen"

#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

#     editors = db.relationship('Building', secondary='chairmenbuildings', backref='editors')

#     def __init__(self, **kwargs):
#         keys = ['userId']

#         for key in keys:
#             setattr(self, key, kwargs.get(key))

    
#     @staticmethod
#     def is_chairman(user_id: int):
#         if(Chairman.query.filter_by(userId=user_id).first() is not None):
#             return True
        
#         return False

# class ChairmenBuildings(db.Model, BaseClass):
#     __tablename__ = "usersflats"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     chairmanId = db.Column(db.Integer, db.ForeignKey('chairmen.id', ondelete='CASCADE'), nullable=False)
#     buildingId = db.Column(db.Integer, db.ForignKey('buildings.id', ondelete='CASCADE'), nullable=False)

#     #__table_args__ = (db.UniqueConstraint('chairmanId', 'buildingId'),)

#     def __init__(self, **kwargs):
#         keys = ['userId', 'buildingId']

#         for key in keys:
#             setattr(self, key, kwargs.get(key))