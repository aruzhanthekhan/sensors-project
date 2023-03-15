from app import db

class UsersFlats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False, index=True)
    flatId = db.Column(db.Integer, nullable=False, index=True)