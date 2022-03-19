from flask import Blueprint, jsonify, request
import jwt
from ..models.user import User
from ..controllers.auth_controller import token_required
from ..controllers.user_controller import index as user_index

from app import app

JSON_MIME_TYPE = 'application/json'

users_app = Blueprint('users_app', __name__)


# this route sends back list of users
@users_app.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    try:
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = User.query.filter_by(public_id=data['public_id']).first()

        if current_user.is_admin:
            return jsonify({
                'users': user_index(),
                'total': len(user_index())
            }), 200

        return jsonify({'error': 'Insufficient permissions'}), 403

    except jwt.ExpiredSignature:
        return jsonify({'error': 'session timed out'}), 401
