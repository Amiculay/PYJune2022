from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_book
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.books_favorited = []

    # C

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (user_name) VALUES (%(user_name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def create_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    # R

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return []
    
    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users[0]
        return []

    @classmethod
    def favorite_users(cls, data):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN books ON books.id = favorites.book_id WHERE user_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        favorites = []
        print(results)
        for result in results:
            book = {
                'id': result['books.id'],
                'title': result['title'],
                'num_pages': result['num_pages'],
                'created_at': result['books.created_at'],
                'updated_at': result['books.updated_at'],
            }
            favorites.append(model_book.Book(book))
        return favorites

    @classmethod
    def unfavorited_users(cls, data):
        query = "SELECT * FROM users WHERE users.id NOT IN ( SELECT user_id FROM favorites WHERE book_id = %(id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return []
    # U
    # D