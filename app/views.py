from app import app
from flask import render_template

CARS_LIMIT = 3

#fictional cars db
cars = {
    "1": {
        "name": "custom car name",
        "model": "audi",
        "mileage": "199999",
        "tank_current": 13,
        "tank_max": 45,
        "fuel_type": "gas",
        "fixes": {
            "1": {
                "cost": 139,
                "description": "Lorem ipsum dolor sit"
            }
        }
    },
    "2": {
        "name": "custom car name",
        "model": "bmw",
        "mileage": "888992",
        "tank_current": 30,
        "tank_max": 70,
        "fuel_type": "gas",
        "fixes": {
            "1": {
                "cost": 3000,
                "description": "Lorem ipsum dolor sit"
            },
            "2": {
                "cost": 1000,
                "description": "Lorem ipsum dolor sit"
            }
        }
    }
}

@app.route('/')
def index():
    """Home page, you can see all your vehicles from there and pick one to manage"""
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Route to add a new vehicle to be managed"""
    return 'add a car'

@app.route('/delete/<string:id>')
def delete(id):
    """Route to delete the existing vehicle from the dashboard"""
    return id

@app.route('/manage/<string:id>')
def manage(id):
    """Route to manage and check vehicle data"""
    return id