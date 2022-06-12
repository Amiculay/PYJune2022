from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default(): # This is going to be our default, 8 by 8
    print("page 1")
    return render_template("test.html")

@app.route('/4')
def secondPage(): # This is going to be our second route, 8 by 4
    return render_template("test.html")

if __name__=="__main__":
    app.run(debug=True, port=24)