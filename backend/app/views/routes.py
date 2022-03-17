from flask import Blueprint, jsonify, request, make_response
import uuid
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from ..controllers.auth_controller import token_required
from ..models.user import User
from app import app, db

JSON_MIME_TYPE = 'application/json'

system_app = Blueprint('system_app', __name__)


# first success on load
@system_app.route('/', methods=['GET'])
def index():
    data = {
        'info': 'Welcome! you can use the v1 section of the API.',
        'status': 200
    }
    return jsonify(data), 200


# this route sends back list of users
@system_app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    # querying the database for all the entries in it
    users = User.query.all()

    # converting the query objects to list of jsons
    output = []

    for user in users:
        output.append({
            'public_id': user.public_id,
            'name': user.name,
            'email': user.email
        })

    return jsonify({'users': output}), 200


@system_app.route('/login', methods=['GET'])
def get_login():
    return jsonify({
        'message': 'Use POST for this route'
    }), 400


# route for logging user in
@system_app.route('/login', methods=['POST'])
def login():
    # creates dictionary of form data
    data = request.form
    errors = []

    if not data:
        errors.append({'input': ['No content is submitted']})

    if not data.get('email'):
        errors.append({'email': ['Your email is required']})

    if not data.get('password'):
        errors.append({'password': ['Your password is required']})

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({
            'errors': errors
        }), 400

    user = User.query.filter_by(email=data.get('email')).first()

    if not user:
        return jsonify({
            'errors': [
                {
                    'email': ['No user found with that email, create a new account']
                }
            ]
        }), 404

    if check_password_hash(user.password, data.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(
            jsonify({
                'message': 'Logged in successfully',
                'user': {
                    'name': user.name,
                    'email': user.email,
                    'is_admin': user.is_admin,
                    'is_developer': user.is_dev,
                    'is_student': user.is_student,
                    'created': user.created_at,
                    'last_update': user.updated_at
                },
                'token': token
            }),
            201
        )

    return jsonify({
        'errors': [
            {
                'password': ['Invalid password provided. Please try again']
            }
        ]
    }), 404


# signup route
@system_app.route('/signup', methods=['POST'])
def signup():
    # creates a dictionary of the form data
    data = request.form
    errors = []

    if not data.get('name'):
        errors.append({'name': ['Your name is required']})

    if not data.get('email'):
        errors.append({'email': ['Your email is required']})

    if not data.get('password'):
        errors.append({'password': ['Your password is required']})

    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({
            'errors': errors
        }), 400

    name, email = data.get('name'), data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin')
    is_dev = data.get('is_dev')
    is_student = data.get('is_student')
    status = data.get('status')
    created_at = datetime.now()
    updated_at = datetime.now()

    # checking for existing user
    user = User.query.filter_by(email=email).first()

    if not user:
        # database ORM object
        user = User(
            public_id=str(uuid.uuid4()),
            name=name,
            email=email,
            password=generate_password_hash(password),
            is_admin=is_admin,
            is_dev=is_dev,
            is_student=is_student,
            status=status,
            created_at=created_at,
            updated_at=updated_at
        )
        # insert user
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'message': 'Successfully registered.'
        }), 201

    else:
        return jsonify({
            'message': 'User already exists. Please log in.'
        }), 202
