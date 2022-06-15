from flask import Flask, render_template, redirect, request
# import the class from User.py
from models.model_user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create_one(request.form)
    return redirect('/users')

@app.route('/users')
def print_users():
    users = User.get_all()
    return render_template("users.html", users = users)

@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_one({'id': id})
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)