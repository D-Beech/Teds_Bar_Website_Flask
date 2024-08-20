from flask import Flask, redirect, url_for, render_template
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


if __name__ == "__main__":
    app.run(debug=True)