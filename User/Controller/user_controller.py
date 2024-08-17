from flask import jsonify

from Exceptions.custom_exceptions import DatabaseOperationError, UserNotFoundError
from User.DTO.user_dto import UserDTO
from User.Service.user_service import UserService

user_service = UserService()


class UserController:
    # Controller: Get all users
    @staticmethod
    def list_users():
        try:
            users = UserService.get_all_users()
            user_dtos = [UserDTO.from_model(user).to_dict() for user in users]
            return jsonify(user_dtos)
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500

    # Controller: Get user by ID
    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            if user:
                user_dto = UserDTO.from_model(user)
                return jsonify(user_dto.__dict__)
            else:
                return jsonify({'error': 'User not found'}), 404
        except UserNotFoundError as e:
            return jsonify({'error': f"User not found: {e}"}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500

    # Controller: Create a new user
    @staticmethod
    def create_user(username, password_hash, email):
        try:
            user = UserService.create_user(username, password_hash, email)
            if user:
                user_dto = UserDTO.from_model(user)
                return jsonify(user_dto.__dict__), 201
            else:
                return jsonify({'error': 'Failed to create user'}), 500
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500

    # Controller: Update user
    @staticmethod
    def update_user(_user):
        try:
            updated_user = UserService.update_user(_user)
            if updated_user:
                user_dto = UserDTO.from_model(updated_user)
                return jsonify(user_dto.__dict__)
            else:
                return jsonify({'error': 'Failed to update user'}), 500
        except UserNotFoundError as e:
            return jsonify({'error': f"User not found: {e}"}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500

    # Controller: Delete user
    @staticmethod
    def delete_user(user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404

            if UserService.delete_user(user):
                return jsonify({'message': 'User deleted successfully'})
            else:
                return jsonify({'error': 'Failed to delete user'}), 500
        except UserNotFoundError as e:
            return jsonify({'error': f"User not found: {e}"}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500
        # Controller: Get user by ID

    @staticmethod
    async def get_user_portfolio_value(user_id,currency):
        try:
            value = await UserService.get_user_portfolio_value(user_id,currency)
            if value:
                return jsonify(value), 200
            else:
                return jsonify({'error': 'Value Not Calculated'}), 404
        except UserNotFoundError as e:
            return jsonify({'error': f"User not found: {e}"}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': f"Database error: {e}"}), 500
        except Exception as e:
            return jsonify({'error': f"Unexpected error: {e}"}), 500
