from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import model_user
from flask_app import DATABASE

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.users_favorited = []

    # C

    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_pages) VALUES (%(title)s, %(num_pages)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def create_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_books = []
            for book in results:
                all_books.append(cls(book))
            return all_books
        return []

    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            all_books = []
            for book in results:
                all_books.append(cls(book))
            return all_books[0]
        return []

    @classmethod
    def favorite_books(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN users ON users.id = favorites.user_id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        favorites = []

        for result in results:
            user = {
                'id': result['users.id'],
                'user_name': result['user_name'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
            }
            favorites.append(model_user.User(user))
        return favorites

    @classmethod
    def unfavorited_books(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE user_id = %(id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            all_books = []
            for book in results:
                all_books.append(cls(book))
            return all_books
        return []
    # U
    # D