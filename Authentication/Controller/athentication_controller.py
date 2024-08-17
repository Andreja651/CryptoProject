from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies

from Authentication.Service.authentication_service import AuthenticationService
from User.Controller.user_controller import UserController

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = AuthenticationService.authenticate_user(username, password)

    if user:
        access_token = create_access_token(identity={'id': user.user_id})
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    resp = jsonify({'message': 'Logout successful'})
    unset_jwt_cookies(resp)
    return resp, 200


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'error': 'Username, password, and email are required'}), 400

    if len(username) < 3:
        return jsonify({'error': 'Username must be at least 3 characters long'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters long'}), 400

    if '@' not in email:
        return jsonify({'error': 'Invalid email address'}), 400

    return UserController.create_user(username=username, password_hash=password, email=email)
