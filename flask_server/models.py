from sqlalchemy.sql import func
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
    phone = db.Column(db.String(255), unique=True, nullable=True, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    dateOfCreate = db.Column(db.DateTime(timezone=True), server_default=func.now())
    dateOfLastUpdate = db.Column(db.DateTime(timezone=True), onupdate=func.now)

    admins = db.relationship('Admin', backref='admins')
    chairmen = db.relationship('Chairman', backref='chairmen')

    def __init__(self, **kwargs):
        keys = ['id', 'firstname', 'lastname', 'patronymic', 'phone', 'email', 'password', 'dateOfCreate', 'dateOfLastUpdate']
        for key in keys:
            setattr(self, key, kwargs.get(key))


chairmenBuildings = db.Table('chairmenBuildings',
    db.Column('chairmanId', db.Integer, db.ForeignKey('chairmen.id')),
    db.Column('buildingId', db.Integer, db.ForeignKey('building.id'))
)


class Admin(db.Model, BaseClass):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    buildings = db.relationship('Building', backref='buildings')

    def __init__(self, **kwargs):
        keys = ['userId']

        for key in keys:
            setattr(self, key, kwargs.get(key))


class Chairman(db.Model, BaseClass):
    __tablename__ = "chairmen"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    editors = db.relationship('Building', secondary='chairmenBuildings', backref='editors')

    def __init__(self, **kwargs):
        keys = ['userId']

        for key in keys:
            setattr(self, key, kwargs.get(key))

    
class Building(db.Model, BaseClass):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(255), unique=True, nullable=False)
    latitude = db.Column(db.Decimal(8, 6), unique=True, nullable=False)
    longitude = db.Column(db.Decimal(9, 6), unique=True, nullable=False)
    hotWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    hotWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    directFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    returnFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputVoltage = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputCurrentStrength = db.Column(db.Float, nullable=False, default=0.0, index=True)
    createdBy = db.Column(db.Integer, db.ForeignKey('admins.id'), nullable=False)
    redactedBy = db.Column(db.Integer, db.ForeignKey('chairmen.id'), nullable=False)
    dateOfCreate = db.Column(db.DateTime(timezone=True), server_default=func.now())
    dateOfLastUpdate = db.Column(db.DataTime(timezone=True), onupdate=func.now())



    def __init__(self, **kwargs):
        keys = ['id', 'owner', 'address', 'hotWaterPressure', 'coldWaterPressure',
                'hotWaterConsumption', 'coldWaterConsumption', 'directFlowTemperature',
                'returnFlowTemperature', 'inputVoltage', 'inputCurrentStrength']
        
        for key in keys:
            setattr(self, key, kwargs.get(key))


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