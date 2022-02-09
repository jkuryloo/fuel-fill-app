from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)

from app import views, models 

with app.app_context():
    db.create_all()