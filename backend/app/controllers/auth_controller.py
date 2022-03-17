from flask import request, jsonify
import jwt
from functools import wraps
from ..models.user import User
from app import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        # return 401 if token is not passed
        if not token:
            return jsonify({
                'error': 'Token is missing!'
            }), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()

            if not current_user:
                return jsonify({
                    'error': 'Session expired!'
                }), 419

        except jwt.ExpiredSignature:
            return jsonify({
                'message': 'Session timed out!',
                'error': 'Token provided is either invalid or expired'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated


class UserAuth:
    # decorator for verifying the JWT
    pass
