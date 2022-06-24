from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE
from flask import flash
from flask_app.models.model_user import User

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users = []
    # C

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, under_thirty, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_thirty)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            all_recipes = []
            for recipe in results:
                all_recipes.append(cls(recipe))
            return all_recipes
        return []

    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def show_recipe_with_user(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipe = cls(results[0])
        for data in results:
            user_data = {
                'id': data['users.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': data['password'],
                'created_at': data['users.created_at'],
                'updated_at': data['users.updated_at']
            }
            recipe.users.append(User(user_data))
        return recipe
    # U

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_thirty = %(under_thirty)s, user_id = %(user_id)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters long.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Recipe description must be at least 3 characters long.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe instructions must be at least 3 characters long.")
            is_valid = False
        if not data['date']:
            flash("Date cannot be blank.")
            is_valid = False
        return is_valid
        