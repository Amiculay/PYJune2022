from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "Coolkid counter demo"

@app.route('/')
def index():
    if 'counter_1' not in session:
        session['counter_1'] = 0
        session['counter_2'] = 0
        session['counter_3'] = 0
        session['counter_4'] = 0
        session['counter_5'] = 0

    return render_template("index.html")

@app.route('/counter/<int:counter>')
def manipulate_counter(counter):
    session[f'counter_{counter}'] += 1
    return redirect('/')

@app.route('/reset')
def reset_counters():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)