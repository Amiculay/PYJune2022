from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users/new')
def new_user():
    return render_template("index.html")

# Create users
@app.route('/create_user', methods=["POST"])
def create_user():
    User.create_one(request.form)
    return redirect('/users')

# Display ALL users
@app.route('/users')
def display_users():
    users = User.get_all()
    return render_template("users.html", users = users)

# Show user
@app.route('/users/<int:id>')
def show_user(id):
    user = User.get_one({'id': id})
    return render_template("read.html", user = user)

# Delete user
@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete_one({'id': id})
    print({'id': id})
    return redirect('/users')

# Show edit page
@app.route('/users/<int:id>/edit')
def edit_user(id):
    user = User.get_one({'id': id})
    return render_template("update.html", user = user)

@app.route('/users/update', methods=['POST'])
def update_user():
    User.update_user(request.form)
    return redirect('/users')