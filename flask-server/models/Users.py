from sqlalchemy import func

from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    patronymic = db.Column(db.String(255), nullable=False, default="Don't have")
    phone = db.Column(db.String(255), nullable=True, index=True)
    email = db.Column(db.String(255), nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    dateOfCreate = db.Column(db.Date, default=func.now())
    dateOfLastUpdate = db.Column(db.Date, default=func.now())