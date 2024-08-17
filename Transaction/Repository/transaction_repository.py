from Exceptions.custom_exceptions import TransactionNotFoundError, DatabaseOperationError
from Transaction.Model.transaction import Transaction
from db_extension import db


class TransactionRepository:
    @staticmethod
    def get_by_id(transaction_id):
        try:
            transaction = Transaction.query.filter_by(transaction_id=transaction_id).first()
            if not transaction:
                raise TransactionNotFoundError(transaction_id)
            return transaction
        except TransactionNotFoundError as e:
            raise e
        except Exception as e:
            raise DatabaseOperationError(f"Error in get_by_id: {e}")

    @staticmethod
    def get_transactions(user_id, currency=None, transaction_type=None):
        try:
            query = db.session.query(Transaction)

            if currency:
                return query.filter(Transaction.currency == currency and Transaction.user_id == user_id)

            if transaction_type:
                return query.filter(Transaction.transaction_type == transaction_type and Transaction.user_id == user_id)

            return query.filter(Transaction.user_id == user_id)

        except Exception as e:
            raise DatabaseOperationError(f"Error in get_by_id: {e}")

    @staticmethod
    def create(transaction):
        try:
            db.session.add(transaction)
            db.session.commit()
            return transaction
        except Exception as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in create: {e}")

    @staticmethod
    def update(transaction):
        try:
            db.session.commit()
            return transaction
        except Exception as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in update: {e}")

    @staticmethod
    def delete(transaction):
        try:
            db.session.delete(transaction)
            db.session.commit()
            return transaction.transaction_id
        except Exception as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Error in delete: {e}")