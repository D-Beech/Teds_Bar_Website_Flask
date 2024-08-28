from flask_sqlalchemy import SQLAlchemy
from classes import *
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY

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



class Cart(db.Model):
    __tablename__ = 'Carts'

    id = db.Column(db.Integer, primary_key=True)
    cart_items = db.Column(ARRAY(db.Integer))

    def __init__(self):
        self.cart_items = []
        pass

    def add_item(self, item_id):
        self.cart_items.append(item_id)
        pass

    def remove_item(self, item_id):
        self.cart_items.remove(item_id)
        pass

    def total_price(self):
        total = 0
        cart = Cart.get_contents(self)
        for x in cart:
            total += x.price
        return total
    
    def empty_cart(self):
        self.cart_items = []

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_contents_as_ids(self):
        return self.cart_items()

    def get_contents(self):
        cart_menu_items = []
        for x in self.cart_items:
            cart_menu_items += MenuItem.query.where(MenuItem.id == x)
        return cart_menu_items
    

class Customer_Details(db.Model):
    __tablename__ = 'Customer_Details'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    pick_up_time = db.Column(db.String(30))

    def __init__(self, firstName, lastName, pickUpTime):
        self.first_name = firstName
        self.last_name = lastName
        self.pick_up_time = pickUpTime        
        pass






class Completed_Order():
    def __init__(self, _cart, _customer_details):
        self.cart = _cart
        self.customer_details = _customer_details
        






