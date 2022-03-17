from flask import Blueprint, jsonify, request, abort

JSON_MIME_TYPE = 'application/json'

system_app = Blueprint('system_app', __name__)

# first success on load
@system_app.route('/', methods=['GET'])
def index():
    data = {
        'info': 'Welcome! you can use the v1 the API.',
        'status': 200
    }
    return jsonify(data), 200