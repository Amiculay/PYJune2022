from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "i am a secret key :)"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/handle_form', methods=["POST"])
def handle_form_input():
    session['email'] = request.form['email_address']
    session['mailing_address'] = request.form['mailing_address']
    session['dob'] = request.form['date_of_birth']
    session['pet'] = request.form['first_pet']
    session['maiden_name'] = request.form['maiden_name']
    session['ssn'] = request.form['social_number']
    return redirect('/form_result')

# When printing a session's key, use the value on the left which is our variable *IN* python
@app.route('/form_result')
def show_result():
    print(session['email'])
    print(session['dob'])
    print(session)
    return render_template("form_result.html") # Renders and posts our date to form_result

if __name__ == "__main__":
    app.run(debug = True)




    """ return render_template("form_result.html",
        email = request.form['email_address'],
        mail_address = request.form['mailing_address'],
        dob = request.form['date_of_birth'],
        first_pet = request.form['first_pet'],
        maiden_name = request.form['maiden_name'],
        ssn = request.form['social_number']
        ) """