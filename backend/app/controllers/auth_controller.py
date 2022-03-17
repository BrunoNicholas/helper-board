from flask import request, jsonify
import jwt
from functools import wraps
from ..models.user import User
from app import app


class UserAuth:
    # decorator for verifying the JWT
    def token_required(self):
        @wraps(self)
        def decorated(*args, **kwargs):
            token = None

            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            # return 401 if token is not passed
            if not token:
                return jsonify({
                    'error': 'Unauthenticated!',
                    'message': 'You are currently not logged in'
                }), 401

            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, app.config['SECRET_KEY'])
                current_user = User.query.filter_by(public_id=data['public_id']).first()

            except ValueError:
                return jsonify({
                    'message': 'Invalid token applied!'
                }), 401

            # returns the current logged-in users' context to the routes
            return self

        return decorated
