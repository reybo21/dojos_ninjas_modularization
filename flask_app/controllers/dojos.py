from flask import Flask, render_template, request, redirect
# import the class from user.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app import app

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("add_dojo.html", all_dojos=dojos)

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", all_dojos=dojos)

@app.route('/dojos/<int:num>')
def display_dojo(num):
    dojo = Dojo.get_by_id(num)
    ninjas = Ninja.from_dojo(num)
    return render_template("display_dojo.html", all_ninjas=ninjas, dojo_name=dojo)

@app.route('/dojos/new/process', methods = ["POST"])
def process_dojo():
    data = { "name" : request.form["name"]}
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/ninjas/new/process', methods = ["POST"])
def process_ninja():
    print (request.form.keys())
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo"]
    }
    print(data)
    Ninja.save(data)
    return redirect('/dojos/{}'.format(request.form["dojo"]))
