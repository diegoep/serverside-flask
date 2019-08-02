from flask_sqlalchemy import SQLAlchemy

from application.enums import UserRole
from application.serialize import Serializer

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data for all models"""
    __abstract__ = True

class User(BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    login = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    userRole = db.Column(db.Enum(UserRole), nullable=False)

    def serialize(self):
        d = Serializer.serialize(self)
        return d

    def __repr__(self):
        return '<User %r>' % self.login