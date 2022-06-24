from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user():

    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():

    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    user = User.get_email(data)

    if not user:
        flash("Invalid login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password")
        return redirect('/')
    session['user_id'] = user.id

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    
    data = {
        'id': session['user_id']
    }

    user = User.get_user_by_id(data)
    recipes = Recipe.show_all()
    return render_template('dashboard.html', user = user, recipes = recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')