from flask import Blueprint, jsonify, request
import jwt
from ..models.user import User
from ..controllers.auth_controller import token_required
from ..controllers.notification_controller import index as notifications_index

from app import app

JSON_MIME_TYPE = 'application/json'

notifications_app = Blueprint('notifications_app', __name__)


# this route sends back list of users
@notifications_app.route('/notifications', methods=['GET'])
@token_required
def get_all_notifications(current_user):
    try:
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = User.query.filter_by(public_id=data['public_id']).first()

        if current_user.is_dev:
            return jsonify({
                'notifications': notifications_index(current_user.id, 'developer'),
                'total': len(notifications_index(current_user.id, 'developer'))
            }), 200

        if current_user.is_student:
            return jsonify({
                'notifications': notifications_index(current_user.id, 'student'),
                'total': len(notifications_index(current_user.id, 'student'))
            }), 200

        if current_user.is_admin:
            return jsonify({
                'notifications': notifications_index(),
                'total': len(notifications_index())
            }), 200

        return jsonify({'error': 'Insufficient permissions'}), 403

    except jwt.ExpiredSignature:
        return jsonify({'error': 'session timed out'}), 401


@notifications_app.route('/notifications', methods=['POST'])
@token_required
def store_location():
    # if request.headers.get('Content-Type') is 'application/json':
    #     data = request.json
    # else:
    #     data = request.form
    data = request.json

    pass
