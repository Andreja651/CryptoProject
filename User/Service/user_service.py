from werkzeug.security import generate_password_hash, check_password_hash

from Exceptions.custom_exceptions import UserNotFoundError, DatabaseOperationError
from User.Model.user import User
from User.Repository.user_repository import UserRepository
from Services.coinApi_service import COINAPIService


class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """
        Gets The user by ID
        :param user_id: The User to be returned
        :return: The User
        """
        try:
            return UserRepository.get_by_id(user_id)
        except UserNotFoundError as e:
            print(f"User not found: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def get_user_by_username(username):
        """
        Gets the User by Username
        :param username: The Username
        :return: The User
        """
        try:
            return UserRepository.get_by_username(username)
        except UserNotFoundError as e:
            print(f"User not found: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def create_user(username, password, email):
        """
        Creates the User
        :param username: The Username for the User
        :param password: The Password for the User
        :param email: The Email for the User
        :return: Created User
        """
        try:
            password_hash = generate_password_hash(password)
            user = User(username=username, password_hash=password_hash, email=email)
            return UserRepository.create(user)
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def update_user(_user):
        """
        Updates the user
        :param _user: The User Model to be Updated
        :return: The Updated User
        """
        try:
            user = UserService.get_user_by_id(_user.user_id)
            if not user:
                raise UserNotFoundError(f"User with ID {_user.user_id} not found.")

            if _user.username:
                user.username = _user.username
            if _user.email:
                user.email = _user.email
            if _user.password and check_password_hash(user.password_hash, _user.password):
                user.password_hash = generate_password_hash(_user.password)

            return UserRepository.update(user)
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def delete_user(user):
        """
        Delets The user
        :param user: The User to be deleted
        :return: The Deleted User ID
        """
        try:
            deleted_usr = UserRepository.delete(user)
            return deleted_usr
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    @classmethod
    def get_all_users(cls):
        """
        Gets All users in the Database
        :return: SQLAlchemy Query
        """
        try:
            return UserRepository.get_all_users()
        except DatabaseOperationError as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def check_password(username, password):
        """
        Checks the passed password and its HASH
        :param username: The Username to find the User
        :param password: The Password passed from Request
        :return: User : None
        """
        user = UserService.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            return user.user_id
        return None

    @staticmethod
    async def get_user_portfolio_value(user_id,currency):
        """
        Calls the COINAPI Service for Portfolio Evaluation
        :param user_id: The ID for the User
        :param currency: The Currency passed from Request
        :return: The calculated Value
        """
        value = await COINAPIService.get_portfolio_value(self=COINAPIService, user_id=user_id,currency=currency)
        if value:
            total_value = sum(detail['value'] for detail in value)
            summary = {
                'total_value': total_value,
                'wallets': {detail['wallet']: {'value': detail['value'], 'currency': detail['currency']} for detail in
                            value}
            }
            return summary
        return None



