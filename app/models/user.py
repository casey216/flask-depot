from flask_login import UserMixin
from app.extensions import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
