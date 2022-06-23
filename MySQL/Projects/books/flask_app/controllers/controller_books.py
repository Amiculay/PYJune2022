from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_book import Book
from flask_app.models.model_user import User

@app.route('/books')
def show_all_books():
    books = Book.show_all()
    return render_template("books.html", books = books)

@app.route('/create/book', methods=['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_pages': request.form['num_pages']
    }
    Book.create_book(data)
    return redirect('/books')

@app.route('/book/favorites/<int:id>')
def favorite_books(id):
    data = {
        'id': id 
    }
    book = Book.show_one(data)
    unfavorited_users = User.unfavorited_users(data)
    favorites = Book.favorite_books(data)
    return render_template('book_favorites.html', book = book, unfavorited_users = unfavorited_users, favorites = favorites)

@app.route('/favorite/by_user', methods=['POST'])
def join_user():
    data = {
        'user_id': request.form['user_id'],
        'book_id': request.form['book_id']
    }
    User.create_favorite(data)
    return redirect(f"/book/favorites/{request.form['book_id']}")