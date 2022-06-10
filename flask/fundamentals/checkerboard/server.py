from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def userDefault(): # Lets just display an 8 by 8
    return render_template("index.html", x = 8, y = 8, evens="red", odds="black")

@app.route('/<int:y>')
def userSingle(y): # Lets just display an 8 by 4
    print("This is the y value", y)
    return render_template("index.html", x = 8, y = y, evens="red", odds="black")

@app.route('/<int:x>/<int:y>')
def userDouble(x, y):
    print(f"x: {x}, y: {y}")
    return render_template("index.html", x = x, y = y, evens="red", odds="black")

@app.route('/<int:x>/<int:y>/<string:evens>')
def userDoubleColor(x, y, evens):
    print(f"x: {x}, y: {y}, evens: {evens}")
    return render_template("index.html", x = x, y = y, evens=evens, odds="black")

@app.route('/<int:x>/<int:y>/<string:evens>/<string:odds>')
def userModular(x, y, evens, odds):
    print(f"x: {x}, y: {y}, evens: {evens}, odds:{odds}")
    return render_template("index.html", x = x, y = y, evens=evens, odds=odds)

if __name__=="__main__":
    app.run(debug=True)