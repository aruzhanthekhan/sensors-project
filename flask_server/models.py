from sqlalchemy import func
from sqlalchemy.inspection import inspect

from app import db

class BaseClass(object):
    """
    Constains common functions like save and delete
    """
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id
    

    def update(self):
        db.session.commit()
        return self.id
    

    def delete(self):
        db.session.delete()
        db.commit()
        return self.id
    

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.key()}
    

    def serialize_list(self, list):
        return [m.serialize() for m in list]
    

class User(db.Model, BaseClass):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    patronymic = db.Column(db.String(255), nullable=False, default="Don't have")
    phone = db.Column(db.String(255), nullable=True, index=True)
    email = db.Column(db.String(255), nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    dateOfCreate = db.Column(db.Date, default=func.now())
    dateOfLastUpdate = db.Column(db.Date, default=func.now())

    def __init__(self, **kwargs):
        keys = ['id', 'firstname', 'lastname', 'patronymic', 'phone', 'email', 'password', 'dateOfCreate', 'dateOfLastUpdate']
        for key in keys:
            setattr(self, key, kwargs.get(key))

    
class Building(db.Model, BaseClass):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String(255), nullable=False, index=True)
    address = db.Column(db.String(255), nullable=False)
    geolocation = db.Column(db.Stirng(255), nullable=False)
    hotWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    hotWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    directFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    returnFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputVoltage = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputCurrentStrength = db.Column(db.Float, nullable=False, default=0.0, index=True)

    def __init__(self, **kwargs):
        keys = ['id', 'owner', 'address', 'hotWaterPressure', 'coldWaterPressure',
                'hotWaterConsumption', 'coldWaterConsumption', 'directFlowTemperature',
                'returnFlowTemperature', 'inputVoltage', 'inputCurrentStrength']
        
        for key in keys:
            setattr(self, key, kwargs.get(key))


class UsersFlats(db.Model, BaseClass):
    __tablename__ = "usersflats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False, index=True)
    flatId = db.Column(db.Integer, nullable=False, index=True)

    __table_args__ = (db.UniqueConstraint('iserId', 'flatId'),)

    def __init__(self, **kwargs):
        keys = ['userId', 'flatId']

        for key in keys:
            setattr(self, key, kwargs.get(key))


class Admin(db.Model, BaseClass):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False, index=True)

    def __init__(self, **kwargs):
        keys = ['userId']

        for key in keys:
            setattr(self, key, kwargs.get(key))


class Chairman(db.Model, BaseClass):
    __tablename__ = "chairmen"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False, index=True)

    def __init__(self, **kwargs):
        keys = ['userId']

        for key in keys:
            setattr(self, key, kwargs.get(key))