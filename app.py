from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/TedsBarAndCafeWebiste-DB'

#Intitialize the database
db = SQLAlchemy(app)
migrate=Migrate(app, db)

#Create db model
class MenuItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    descrption = db.Column(db.String(200))
    price = db.Column(db.Numeric, nullable=False)
    
    #Returns a string when we add an item
    def __repr__(self):
        return '<Name %r>' % self.id






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
        new_item = MenuItems(name=item_name, descrption=item_description, price=item_price)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/addItem')
        except:
            return "There was an error adding the item"
            

    else:
        menu_items = MenuItems.query.all()
        return render_template("addItem.html", stuff=menu_items)

if __name__ == "__main__":
    app.run(debug=True)