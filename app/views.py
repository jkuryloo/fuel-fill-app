from app import app, db 
from flask import render_template, request, redirect, url_for, flash
from .models import Car, FillUp, Fix
from string import ascii_letters
from random import choice

def generate_id(text):
    return text + "".join([choice(ascii_letters) for _ in range(5)])

def add_car(name, description, mileage, capacity, fuel):
    car = Car(
        id = generate_id(name),
        name = name,
        mileage = mileage,
        capacity = capacity,
        fuel_type = fuel
    )
    if description:
        car.description = description
    db.session.add(car)
    db.session.commit()
    return

def update_car(car: Car, name, description, mileage, capacity, fuel):
    car.name = name 
    car.description = description
    car.mileage = mileage 
    car.capacity = capacity 
    car.fuel = fuel 
    db.session.commit()
    return 

def add_fill_up(car: Car, gas, price):
    gas = float(gas)
    price = float(price)

    fill_up = FillUp(
        car_id = car.id,
        amount = gas,
        price = price,
        total = round(gas * price, 2)
    )

    car.total_fill_ups += 1
    car.total_gas_refilled += gas
    car.total_spend += round(gas * price, 2)

    db.session.add(fill_up)
    db.session.commit()
    return

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page, you can see all your vehicles from there and pick one to manage its data"""
    cars = db.session.query(Car).all()
    if request.method == 'POST':
        if 'car-name' in request.form:
            add_car(
                request.form.get('car-name'),
                request.form.get('car-description'),
                request.form.get('car-mileage'),
                request.form.get('car-capacity'),
                request.form.get('car-fuel')
            )
            flash('Car has been added successfully', 'success')
            return redirect(url_for('index'))
    return render_template('index.html', cars=cars)

@app.route('/delete/<string:id>')
def delete(id):
    """Route to delete the existing vehicle from the dashboard"""
    car = Car.query.filter_by(id=id).first()
    if car:
        db.session.delete(car)
        db.session.commit()
        flash('Car deleted successfully', 'success')
    else:
        flash('This car does not exist', 'danger')
    return redirect(url_for('index'))

@app.route('/manage/<string:id>', methods=['GET', 'POST'])
def manage(id):
    """Route to manage and check vehicle data"""
    car = Car.query.filter_by(id=id).first()

    if request.method == 'POST':
        if 'car-name' in request.form:
            update_car(
                car,
                request.form.get('car-name'),
                request.form.get('car-description'),
                request.form.get('car-mileage'),
                request.form.get('car-capacity'),
                request.form.get('car-fuel')
            )
            flash('Your car\'s data has been updated', 'success')
        if 'add-fill-up-gas' in request.form:
            add_fill_up(
                car,
                request.form.get('add-fill-up-gas'),
                request.form.get('add-fill-up-price'),
            )
            flash('Your car has been filled up successfully', 'success')
    if car:
        fill_ups = FillUp.query.filter_by(car_id=id).order_by(FillUp.date.desc()).all()
        return render_template('manage.html', car=car, fill_ups=fill_ups)
    else:
        flash('This car does not exist', 'danger')

    return redirect(url_for('index'))