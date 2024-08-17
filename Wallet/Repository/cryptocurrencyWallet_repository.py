from Exceptions.custom_exceptions import DatabaseOperationError
from db_extension import db
from Wallet.Model.cryptocurrencyWallet import CryptocurrencyWallet
from sqlalchemy.exc import SQLAlchemyError


class CryptocurrencyWalletRepository:
    @staticmethod
    def get_by_id(wallet_id):
        try:
            return CryptocurrencyWallet.query.get(wallet_id)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to get wallet with ID {wallet_id}: {e}")

    @staticmethod
    def get_all_wallets():
        try:
            return CryptocurrencyWallet.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to retrieve all wallets: {e}")

    @staticmethod
    def get_by_user_and_currency(user_id, currency):
        try:
            return CryptocurrencyWallet.query.filter_by(user_id=user_id, currency=currency).first()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to get wallet for user {user_id} and currency {currency}: {e}")

    @staticmethod
    def get_all_by_user(user_id):
        try:
            return CryptocurrencyWallet.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to get wallets for user {user_id}: {e}")

    @staticmethod
    def create(wallet):
        try:
            db.session.add(wallet)
            db.session.commit()
            return wallet
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to create wallet: {e}")

    @staticmethod
    def update(wallet):
        try:
            db.session.commit()
            return wallet
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to update wallet: {e}")

    @staticmethod
    def delete(wallet):
        try:
            db.session.delete(wallet)
            db.session.commit()
            return wallet.wallet_id
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseOperationError(f"Failed to delete wallet: {e}")