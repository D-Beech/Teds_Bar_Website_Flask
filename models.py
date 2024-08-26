from flask_sqlalchemy import SQLAlchemy
from classes import *
from datetime import datetime

#Database
db = SQLAlchemy()

#This is the base class
class MenuItem(db.Model):

    __tablename__ = 'MenuItems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Numeric, nullable=False)
    img_path = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'MenuItem',
    }


#Child classes of MenuItem
#implementing joined table inhertance seems like the easiest option in SQLAlchemy
class Burger(MenuItem):
    __tablename__ = 'Burger'
    id = db.Column(db.Integer, db.ForeignKey('MenuItems.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'Burger',
    }

class Snack(MenuItem):
    __tablename__ = 'Snack'
    id = db.Column(db.Integer, db.ForeignKey('MenuItems.id'), primary_key=True)
    specialty = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity': 'Snack',
    }

class Coffee(MenuItem):
    __tablename__ = 'Coffee'
    id = db.Column(db.Integer, db.ForeignKey('MenuItems.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'Coffee',
    }

class Beer(MenuItem):
    __tablename__ = 'Beer'
    id = db.Column(db.Integer, db.ForeignKey('MenuItems.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'Beer',
    }

class Wine(MenuItem):
    __tablename__ = 'Wine'
    id = db.Column(db.Integer, db.ForeignKey('MenuItems.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'Wine',
    }



#Cart Class
# class Cart(db.Model):
#     __tablename__="Cart"
#     id = db.Column(db.Integer, primary_key=True)

class Completed_Order():
    def __init__(self, _cart, _customer_details):
        self.cart = _cart
        self.customer_details = _customer_details
        






