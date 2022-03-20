from flask import Blueprint, jsonify, request
import jwt
from ..models.user import User
from ..controllers.auth_controller import token_required
from ..controllers.message_controller import index as messages_index

from app import app

JSON_MIME_TYPE = 'application/json'

messages_app = Blueprint('messages_app', __name__)


# this route sends back list of users
@messages_app.route('/messages', methods=['GET'])
@token_required
def get_all_messages(current_user):
    try:
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'])
        current_user = User.query.filter_by(public_id=data['public_id']).first()

        if current_user.is_dev:
            return jsonify({
                'messages': messages_index(current_user.id, 'developer'),
                'total': len(messages_index(current_user.id, 'developer'))
            }), 200

        if current_user.is_student:
            return jsonify({
                'messages': messages_index(current_user.id, 'student'),
                'total': len(messages_index(current_user.id, 'student'))
            }), 200

        if current_user.is_admin:
            return jsonify({
                'messages': messages_index(),
                'total': len(messages_index())
            }), 200

        return jsonify({'error': 'Insufficient permissions'}), 403

    except jwt.ExpiredSignature:
        return jsonify({'error': 'session timed out'}), 401


@messages_app.route('/messages', methods=['POST'])
@token_required
def store_message():
    if request.headers.get('Content-Type') is 'application-json':
        data = request.json
    else:
        data = request.form

    pass
