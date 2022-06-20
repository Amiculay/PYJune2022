from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.model_dojo import Dojo

@app.route('/') # Redirects to main
def index():
    return redirect('/read_dojos')

@app.route('/read_dojos') #Show dojos
def dojo_new():
    all_dojos = Dojo.get_all_dojos()
    print(all_dojos[0].id) # Testing to see which dojo I get
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/dojo_form/submit', methods=['POST']) # Posts form to database
def submit_dojo_form():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/read_dojos')