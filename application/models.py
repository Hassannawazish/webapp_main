from application.init import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, text, Float, Boolean, ForeignKey

from sqlalchemy import Column, Integer, Text, text, Float, Boolean, ForeignKey
from sqlalchemy.orm import backref, relationship
from database.setup import Base

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    firstname = Column(String(64), index=True)
    lastname = Column(String(64), index=True)
    address = Column(String(64), unique=True, index=True)
    number = Column(String(64), unique=True, index=True)
    gender = Column(String(64))
    password_hash = Column(String(128))

    def __init__(self, email, firstname, lastname, address, number, gender, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.number = number
        self.gender = gender
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
