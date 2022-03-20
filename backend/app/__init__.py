from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import sys
import os

app = Flask(__name__)
CORS(app)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SECRET_KEY'] = 'MMOQLDpZOgsF1sFjx4nitkbheSNzPqGIt1+X3h1vPPQ='
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bruno:dollar@localhost/db_test_py'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .models.user import User
from .models.message import Message
from .models.location import Location
from .models.notification import Notification

from .views.routes import system_app
from .views.r_users import users_app
from .views.r_messages import messages_app
from .views.r_locations import locations_app
from .views.r_notifications import notifications_app

# db.create_all()
migrate = Migrate(app, db)

app.register_blueprint(system_app, url_prefix="/api/v1")
app.register_blueprint(users_app, url_prefix="/api/v1")
app.register_blueprint(messages_app, url_prefix="/api/v1")
app.register_blueprint(locations_app, url_prefix="/api/v1")
app.register_blueprint(notifications_app, url_prefix="/api/v1")


@app.route('/', methods=['GET'])
def welcome():
    data = {
        'info': 'welcome please follow the app documentation to proceed',
        'status': 206
    }
    return jsonify(data), 206


@app.route('/api', methods=['GET'])
@app.route('/api/', methods=['GET'])
def api_route():
    data = {
        'info': 'you are close, add a version to proceed',
        'status': 206
    }
    return jsonify(data), 206


# Handling of route errors
@app.errorhandler(400)
def bad_request(error):
    """
    Gives error message when any bad requests are made.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 400}), 400


@app.errorhandler(404)
def not_found(error):
    """
    Gives error message when any invalid url are requested.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 404}), 404


@app.errorhandler(403)
def not_allowed(error):
    """
    Gives error message when a resource is restricted from the user access.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 403}), 403


@app.errorhandler(500)
def server_error(error):
    """
    Gives error message when a resource is restricted from the user access.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 500}), 500


@app.errorhandler(504)
def server_timeout(error):
    """
    Gives error message when a resource is restricted from the user access.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 504}), 504
