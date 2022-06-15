from flask import Flask, render_template
# import the class from friend.py
from models.model_user import User
app = Flask(__name__)

# THIS CHANGES LOCATION *****************************
@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True)