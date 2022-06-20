from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.monster_model import Monster

# ============== FORM ROUTES ==============

@app.route('/')
@app.route('/monster_form')
def show_monster_form():
    return render_template('create_monster.html')

@app.route('/monster_form/submit', methods = ['POST'])
def submit_monster_form():
    data = {
        'monster_name': request.form['monster_name'],
        'monster_habitat': request.form['monster_habitat'],
        'monster_age': request.form['monster_age']
    }
    Monster.create_one_monster(data)
    return redirect('/monster_form')

# ============== DISPLAY ROUTES ==============

@app.route('/all_monsters')
def display_all_monsters():
    all_monsters = Monster.get_all_monsters()
    return render_template('all_monsters.html', all_monsters = all_monsters) 

@app.route('/monster/<int:monster_id>')
def display_one_monster(monster_id):
    data = {
        'monster_id': monster_id
    }
    monster = Monster.get_one_monster(data)
    return render_template('show_monster.html', monster = monster)

# ============== EDIT ROUTES ==============

@app.route('/monster/edit_form/<int:monster_id>')
def edit_monster_form(monster_id):
    data = {
        'monster_id': monster_id
    }
    one_monster = Monster.get_one_monster(data)
    return render_template('edit_monster.html', monster = one_monster)

@app.route('/monster/edit_one_monster/<int:monster_id>', methods=['POST'])
def edit_one_monster(monster_id):
    data = {
        'monster_name': request.form['monster_name'],
        'monster_habitat': request.form['monster_habitat'],
        'monster_age': request.form['monster_age'],
        'monster_id': monster_id
    }

    Monster.edit_one_monster(data)

    return redirect('/all_monsters')

# ============== EDIT ROUTES ==============

@app.route('/monster/delete/<int:monster_id>')
def delete_one_monster(monster_id):
    data = {
        'monster_id': monster_id
    }
    Monster.delete_one_monster(data)
    return redirect('/all_monsters')