from datetime import datetime
from app.extensions import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    customer_since = db.Column(db.Date)
    loyalty_points = db.Column(db.Integer)

    def __repr__(self):
        return f'<Customer {self.id}>'

class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    company_name = db.Column(db.String(100))
    contract_start = db.Column(db.Date)

    def __repr__(self):
        return f'<Vendor {self.company_name}>'

class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    license_number = db.Column(db.String(50))
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'))
    status = db.Column(db.String(20))

    def __repr__(self):
        return f'<Driver {self.id}>'

class Truck(db.Model):
    __tablename__ = 'truck'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    capacity = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(20))

    def __repr__(self):
        return f'<Truck {self.license_plate}>'
