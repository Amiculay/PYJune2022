from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:y>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<string:evens>')
@app.route('/<int:x>/<int:y>/<string:evens>/<string:odds>')
def userModular(x = 8, y = 8, evens = 'red', odds = 'black'):
    print(f"x: {x}, y: {y}, evens: {evens}, odds:{odds}")
    return render_template("index.html", x = x, y = y, evens=evens, odds=odds)

@app.route('/userprofile/<int:user_id>')
@app.route('/userprofile/<string:username>')
def userProfile(user_id = None, username = None)


if __name__=="__main__":
    app.run(debug=True)