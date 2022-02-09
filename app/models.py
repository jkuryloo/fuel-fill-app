from app import db 
from datetime import datetime

class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100), default='Why not adding some description? Click manage button!')
    mileage = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    fuel_type = db.Column(db.String(100))
    total_fill_ups = db.Column(db.Integer, default=0)
    total_gas_refilled = db.Column(db.Integer, default=0)
    total_spend_fill_ups = db.Column(db.Integer, default=0)
    fill_ups = db.relationship('FillUp', backref='car', lazy='dynamic')
    total_fixes = db.Column(db.Integer, default=0)
    total_spend_fixes = db.Column(db.Integer, default=0)
    fixes = db.relationship('Fix', backref='car', lazy='dynamic')

class FillUp(db.Model):
    __tablename__ = "fill_ups"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.String(20), db.ForeignKey('cars.id'))
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    total = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow())

class Fix(db.Model):
    __tablename__ = "fixes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.String(20), db.ForeignKey('cars.id'))
    description = db.Column(db.String(1000))
    total = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow())