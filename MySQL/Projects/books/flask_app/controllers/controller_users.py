from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_user import User
from flask_app.models.model_book import Book

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def show_all_users():
    users = User.show_all()
    return render_template('users.html', users = users)

@app.route('/create/user', methods=['POST'])
def create_user():
    data = {
        'user_name': request.form['user_name']
    }
    User.create_user(data)
    return redirect('/users')

@app.route('/user/favorites/<int:id>')
def favorites(id):
    data = {
        'id': id
    }
    user = User.show_one(data)
    unfavorited_books = Book.unfavorited_books(data)
    favorites = User.favorite_users(data)
    return render_template("user_favorites.html", user = user, unfavorited_books = unfavorited_books, favorites = favorites)

@app.route('/favorite/by_book', methods=['POST'])
def join_book():
    data = {
        'user_id': request.form['user_id'],
        'book_id': request.form['book_id']
    }
    User.create_favorite(data)
    return redirect(f"/user/favorites/{request.form['user_id']}")