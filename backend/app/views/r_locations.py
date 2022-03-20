from flask import Blueprint, jsonify, request
import jwt
from ..models.user import User
from ..controllers.auth_controller import token_required
from ..controllers.location_controller import index as locations_index

from app import app

JSON_MIME_TYPE = 'application/json'

locations_app = Blueprint('locations_app', __name__)


# this route sends back list of users
@locations_app.route('/locations', methods=['GET'])
@token_required
def get_all_locations(current_user):
    try:
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = User.query.filter_by(public_id=data['public_id']).first()

        if current_user.is_admin:
            return jsonify({
                'locations': locations_index(),
                'total': len(locations_index())
            }), 200

        return jsonify({'error': 'Insufficient permissions'}), 403

    except jwt.ExpiredSignature:
        return jsonify({'error': 'session timed out'}), 401


@locations_app.route('/locations', methods=['POST'])
@token_required
def store_location():
    # if request.headers.get('Content-Type') is 'application/json':
    #     data = request.json
    # else:
    #     data = request.form
    data = request.json

    pass
