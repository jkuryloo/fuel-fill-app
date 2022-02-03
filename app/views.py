from app import app
from flask import render_template, request, redirect, url_for, flash
from string import ascii_letters
from random import choice

#cars "database"
cars = {}

def generate_id(name):
    return name + "".join([choice(ascii_letters) for _ in range(5)])

def add_car(id, name, description, mileage, capacity, fuel):
    if not description:
        description = "Why not adding some description? Click manage button!"
    cars[id] = {
        "name": name,
        "description": description,
        "mileage": mileage,
        "capacity": capacity,
        "fuel_type": fuel,
        "fixes": {}
    }
    return flash('Car added successfully', 'success')

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page, you can see all your vehicles from there and pick one to manage its data"""
    if request.method == 'POST':
        if 'car-name' in request.form:
            add_car(
                generate_id(request.form.get('car-name')),
                request.form.get('car-name'),
                request.form.get('car-description'),
                request.form.get('car-mileage'),
                request.form.get('car-capacity'),
                request.form.get('car-fuel')
            )
    return render_template('index.html', cars=cars)

@app.route('/delete/<string:id>')
def delete(id):
    """Route to delete the existing vehicle from the dashboard"""
    if id in cars:
        del cars[id]
        flash('Car deleted successfully', 'success')
    else:
        flash('This car does not exist', 'danger')
    return redirect(url_for('index'))

@app.route('/manage/<string:id>')
def manage(id):
    """Route to manage and check vehicle data"""
    if id in cars:
        return render_template('manage.html', car=cars[id])
    else:
        flash('This car does not exist', 'danger')
    return redirect(url_for('index'))