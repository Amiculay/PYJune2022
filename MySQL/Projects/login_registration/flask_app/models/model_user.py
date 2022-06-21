from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import DATABASE
from flask import flash
import re
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"^[a-zA-z,'-. ]+$")
PASSWORD_REGEX = re.compile(r"")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password'] # This should be hashed
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.full_name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
    
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return User(results[0])
        return []
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 2: # Checks length of first name
            flash("Invalid first name, must have more than 2 characters and cannot have numbers.")
            is_valid = False
        if len(data['last_name']) < 2: # Checks length of last name
            flash("Invalid last name, must have more than 2 characters and cannot have numbers.")
            is_valid = False
        if not NAME_REGEX.match(data['first_name']): # Checks if the first name is valid
            flash("Invalid first name, cannot contain numbers.")
            is_valid = False
        if not NAME_REGEX.match(data['last_name']): # Checks if the last name is valid
            flash("Invalid last name, cannot contain numbers.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Invalid password, must be longer than 8 characters.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords must match")
            is_valid = False
        if User.get_email(data): # Checks if the email already exists (if its true, it exists)
            flash("This email already exists.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): # Checks if the email is valid
            flash("Invalid email, please try again.")
            is_valid = False
        
        return is_valid
