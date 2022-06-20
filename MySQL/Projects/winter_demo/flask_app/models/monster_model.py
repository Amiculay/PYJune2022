from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Monster:
    def __init__(self, data):
        self.id = data['id']
        self.monster_name = data['monster_name']
        self.monster_habitat = data['monster_habitat']
        self.monster_age = data['monster_age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_one_monster(cls, data):
        query = "INSERT INTO monsters (monster_name, monster_habitat, monster_age) VALUES (%(monster_name)s, %(monster_habitat)s, %(monster_age)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_monsters(cls):
        query = "SELECT * FROM monsters;"
        results = connectToMySQL(DATABASE).query_db(query) # List of dictionaries
        print(results)
        all_monsters = []

        for row in results:
            all_monsters.append(cls(row))
        return all_monsters

    @classmethod
    def get_one_monster(cls, data):
        query = "SELECT * FROM monsters where id = %(monster_id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def edit_one_monster(cls, data):
        query = "UPDATE * FROM monsters SET monster_name = %(monster_name)s, monster_habitat = %(monster_habitat)s, monster_age = %(monster_age)s WHERE id = %(monster_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_monster(cls, data):
        query = "DELETE FROM monsters where id = %(monster_id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)