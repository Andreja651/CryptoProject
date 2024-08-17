from Exceptions.custom_exceptions import UserNotFoundError, DatabaseOperationError
from db_extension import db
from User.Model.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserRepository:
    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                raise UserNotFoundError(user_id)
            return user
        except SQLAlchemyError as e:
            raise DatabaseOperationError(f"Error in get_by_id: {e}")

    @staticmethod
    def get_by_username(username):
        try:
            user = User.query.filter_by(username=username).first()
            if not user:
                raise UserNotFoundError(username)
            return user
        except SQLAlchemyError as e:
            raise DatabaseOperationError(f"Error in get_by_username: {e}")

    @staticmethod
    def create(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in create: {e}")

    @staticmethod
    def update(user):
        try:
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in update: {e}")

    @staticmethod
    def delete(user):
        try:
            db.session.delete(user)
            db.session.commit()
            return user.user_id
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in delete: {e}")

    @classmethod
    def get_all_users(cls):
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            raise DatabaseOperationError(f"Error in get_all_users: {e}")