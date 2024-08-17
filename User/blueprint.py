from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from User.Controller.user_controller import UserController
from User.DTO.user_dto import UserDTO

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


# Controller: Get all users
@user_bp.route('/', methods=['GET'])
@jwt_required()
def list_users():
    return UserController.list_users()


# Controller: Get user by ID
@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    if get_jwt_identity() is not None:
        current_user = get_jwt_identity()
        user_id = current_user['id']

    return UserController.get_user_by_id(user_id)


# Controller: Update user
@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = UserDTO
    if get_jwt_identity() is not None:
        current_user = get_jwt_identity()
        user_id = current_user['id']

    data = request.get_json()
    user.user_id = user_id
    user.username = data.get('username')
    user.email = data.get('email')
    user.password = data.get('password')

    return UserController.update_user(user)


# Controller: Delete user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    if get_jwt_identity() is not None:
        current_user = get_jwt_identity()
        user_id = current_user['id']
    return UserController.delete_user(user_id)


# Controller: Get Portfolio Value
@user_bp.route('/portfolio-value/<int:user_id>', methods=['GET'])
@jwt_required()
async def get_portfolio_value(user_id):
    if get_jwt_identity() is not None:
        current_user = get_jwt_identity()
        user_id = current_user['id']
    data = request.get_json()
    currency = data.get('currency', 'USD')
    return await UserController.get_user_portfolio_value(user_id, currency)
