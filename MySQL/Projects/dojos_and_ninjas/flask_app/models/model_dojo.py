from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.model_ninja import Ninja

# Initialize dojo and its attributes
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # C

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            all_dojos = []
            for dojo in results:
                all_dojos.append(cls(dojo))
            return all_dojos
        return []

    @classmethod # Regular join
    def get_one_dojo(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DATABASE).query_db(query)
        return cls(results[0])

    @classmethod # One to many LEFT JOIN, shows all ninjas under specific dojo
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
                'id': data['ninjas.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'age': data['age'],
                'created_at': data['ninjas.created_at'],
                'updated_at': data['ninjas.updated_at'],
                'dojo_id': data['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo