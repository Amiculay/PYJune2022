from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "we stay a secret because we're gs like lasagna"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/handle_results', methods=["POST"])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['favorite_language']
    session['comment'] = request.form['comments']
    return redirect("/result")

@app.route('/result')
def show_result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True)