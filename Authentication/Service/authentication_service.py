from User.Service.user_service import UserService
from Exceptions.custom_exceptions import UserNotFoundError


class AuthenticationService:

    @staticmethod
    def authenticate_user(username, password):
        """
        Authenticate the user for login and token distribution
        :rtpe: object
        """
        try:
            user_id = UserService.check_password(username, password)
            if user_id is not None:
                return user_id
        except UserNotFoundError as e:
            print(f"User not found: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
