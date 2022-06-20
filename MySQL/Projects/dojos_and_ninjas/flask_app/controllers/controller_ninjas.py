from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/create/new_ninja') # Creating a ninja, needs all the data to test and fill in
def display_ninja():
    ninjas = Ninja.get_all_ninjas()
    all_dojos = Dojo.get_all_dojos()
    return render_template('new_ninjas.html', ninjas = ninjas, all_dojos = all_dojos)

@app.route('/ninja_form/submit', methods=['POST']) # Takes user's input values and posts to database
def submit_ninja_form():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/create/new_ninja')

@app.route('/show_ninjas/dojo/<int:id>') # Route to show ninjas in specific dojos
def show(id):
    data = {
        'id': id
    }
    ninjas = Dojo.get_dojo_with_ninjas(data)
    print(ninjas.ninjas)
    return render_template('dojo_show.html', ninjas = ninjas)