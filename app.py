from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
from classes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/TedsBarAndCafeWebiste-DB'

#Intitialize the database
db.init_app(app)
migrate=Migrate(app, db)

#Initialize Cart
cart = Cart()

#Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/order")
def order():
    return render_template("order.html")



#This is a simple API I am using to learn flask and develop the item gallery/db, it will be removed
@app.route("/addItem", methods=['POST','GET'])
def addItem():

    if request.method == "POST":
        item_name = request.form['name']
        item_description = request.form['description']
        item_price = request.form['price']
        new_item = Burger(name=item_name, description=item_description, price=item_price)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/addItem')
        except:
            return "There was an error adding the item"
    else:
        menu_items = MenuItem.query.all()
        return render_template("addItem.html", stuff=menu_items, cartItems=cart.get_contents(), cartTotal=cart.total_price())

#Cart APPIS    
@app.route("/add", methods=['POST'])
def add_to_cart():
    item_id = request.form['itemId']
    cart.add_item(item_id)
    return redirect('/addItem')

@app.route("/remove", methods=['POST'])
def remove_from_cart():
    item_id = request.form['itemId']
    cart.remove_item(item_id)
    return redirect('/addItem')

@app.route("/empty", methods=['POST'])
def empty_cart():
    cart.save_to_db()
    cart.empty_cart()
    return redirect('/addItem')

#main
if __name__ == "__main__":
    app.run(debug=True)