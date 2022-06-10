from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def levelOne():
    return render_template("index.html", boxes = 3, color = "blue", level = 1)
    
@app.route('/play/<int:number>')
def levelTwo(number):
    return render_template("index.html", boxes = number, color = "blue", level = 2)

@app.route('/play/<int:number>/<string:color>')
def levelThree(number, color):
    return render_template("index.html", boxes = number, color = color, level = 3)

if __name__=="__main__":
    app.run(debug=True)