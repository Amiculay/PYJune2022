from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # C

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            all_ninjas = []
            for ninja in results:
                all_ninjas.append(cls(ninja))
            return all_ninjas
        return []

    @classmethod
    def get_one_ninja(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL(DATABASE).query_db(query)
        return cls(results[0])
        
    # @classmethod
    # def get_ninjas_from_dojo(cls, data):
    #     query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    #     if results:
    #         ninjas = cls(results[0])
    #         dojo_data = {
    #             'id': results[0]['dojos.id'],
    #             'name': results[0]['dojos.name'],
    #             'created_at': results[0]['dojos.created_at'],
    #             'updated_at': results[0]['dojos.updated_at']
    #         }
    #         dojo = Dojo(dojo_data)
    #         return ninjas
