from app import db

class Flats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(255), nullable=False, index=True)
    address = db.Column(db.String(255), nullable=False)
    hotWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterPressure = db.Column(db.Float, nullable=False, default=0.0, index=True)
    hotWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    coldWaterConsumption = db.Column(db.Float, nullable=False, default=0.0, index=True)
    directFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    returnFlowTemperature = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputVoltage = db.Column(db.Float, nullable=False, default=0.0, index=True)
    inputCurrentStrength = db.Column(db.Float, nullable=False, default=0.0, index=True)