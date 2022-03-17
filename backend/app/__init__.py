from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bruno:dollar@localhost/db_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db.create_all()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .models.user import User
from .models.message import Message

from .views.routes import system_app

app.register_blueprint(system_app, url_prefix="/api/v1")
