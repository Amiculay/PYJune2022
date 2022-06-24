from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User

@app.route('/recipe/form')
def show_recipe_form():
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')

    return render_template('create_recipe.html')

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/form')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'under_thirty': request.form['under_thirty'],
        'user_id': request.form['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/show/recipe/<int:id>')
def show_one_recipe(id):
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.show_recipe_with_user(data)
    user = User.get_user_by_id({'id': session['user_id']})
    return render_template('show_recipe.html', recipe = recipe, user = user)

@app.route('/edit/form/<int:id>')
def edit_recipe(id):
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.show_recipe_with_user(data)
    return render_template('update_recipe.html', recipe = recipe)

@app.route('/update/recipe/<int:id>', methods=['POST'])
def update_recipe(id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/form/{id}")
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'under_thirty': request.form['under_thirty'],
        'user_id': request.form['user_id']
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')

@app.route('/delete/recipe/<int:id>', methods=['GET'])
def delete_recipe(id):
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    data = {
        'id': id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')