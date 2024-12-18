from datetime import datetime
from app.extensions import db

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(15))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    users = db.relationship('User', backref='person', lazy=True)
    customers = db.relationship('Customer', backref='person', lazy=True)
    vendors = db.relationship('Vendor', backref='person', lazy=True)
    drivers = db.relationship('Driver', backref='person', lazy=True)
    roles = db.relationship('Role', secondary='person_role', backref='persons')

    def __repr__(self):
        return f'<Person {self.firstname} {self.lastname}>'
