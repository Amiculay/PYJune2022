from flask import Flask, render_template, request, redirect; import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # Get data
    strawberries = int(request.form['strawberry'])
    blackberries = int(request.form['blackberry'])
    raspberries = int(request.form['raspberry'])
    apples = int(request.form['apple'])
    count = strawberries + blackberries + raspberries + apples
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    time_func = datetime.datetime.now()
    time = time_func.strftime("%B %d %Y %I:%M:%S %p")
    print(request.form)
    # Return data for post
    return render_template("checkout.html",
    strawberries = strawberries,
    blackberries = blackberries,
    raspberries = raspberries,
    apples = apples,
    count = count,
    first_name = first_name,
    last_name = last_name,
    student_id = student_id,
    time = time
    )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    