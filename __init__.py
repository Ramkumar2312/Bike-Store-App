from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from sqlalchemy_utils.functions import database_exists

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




from bikestore.models import Bike_order,Bike_inventory
from bikestore import routes

if database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    pass
else:
    db.create_all()
    db.session.commit()