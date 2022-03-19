from flask import Blueprint, jsonify, request
import jwt
from ..models.user import User
from ..controllers.auth_controller import token_required
from ..controllers.user_controller import UserController

from app import app

JSON_MIME_TYPE = 'application/json'

locations_app = Blueprint('locations_app', __name__)


# this route sends back list of users
@locations_app.route('/locations', methods=['GET'])
@token_required
def get_all_registered_locations(current_user):
    try:
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = User.query.filter_by(public_id=data['public_id']).first()

        if current_user.is_admin:
            users = index()
            return jsonify({'users': users}), 200

        return jsonify({'error': 'Insufficient permissions'}), 403

    except jwt.ExpiredSignature:
        return jsonify({'error': 'session timed out'}), 401
