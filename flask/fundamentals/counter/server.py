from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "i dont know what a secret key does"

@app.route('/')
def index():
    if 'counter_1' not in session:
        session['counter_1'] = 0 # Initialize clicker counter
        session['counter_2'] = 0 # Initialize visit counter
    session['counter_2'] += 1
    return render_template("index.html", visits = session['counter_2']) # We do not have to return session, only did it to make it easier to recognize

@app.route('/counter')
def increment_one():
    session['counter_1'] += 1 # Increment by 1
    session['counter_2'] -= 1 # Because we increment by 1 everything we go back to home page, decrement visit counter by 1 to cancel out
    return redirect('/')

@app.route('/counter/2')
def increment_two():
    session['counter_1'] += 2
    session['counter_2'] -= 1
    return redirect('/')

# Making our own counter?
""" 
@app.route('/', methods=['POST'])
def user_counter():
    value = request.form('user_number')
    print(value)
    session['counter_1'] += value
    return render_template("index.html", value = value)
 """
 
@app.route('/reset')
def reset_clicks():
    session['counter_1'] = 0 # Resets the clicker counter
    session['counter_2'] -= 1 # We do not want to reset the visit counter here
    return redirect('/')

@app.route('/destroy_session')
def destroy_everything():
    session.clear() # Reset literally EVERYTHING (Clears session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)