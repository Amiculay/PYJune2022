from flask import Flask
app = Flask(__name__)
app.secret_key = "custom_key"

DATABASE = 'dojos_and_ninjas'