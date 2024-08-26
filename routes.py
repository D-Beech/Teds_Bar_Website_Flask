from flask import Flask, render_template

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