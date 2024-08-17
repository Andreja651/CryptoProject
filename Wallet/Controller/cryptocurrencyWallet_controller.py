from flask import jsonify

from Exceptions.custom_exceptions import WalletDeletionError, WalletUpdateError, WalletCreationError, \
    WalletNotFoundError
from Services.coinApi_service import COINAPIService
from Wallet.Service.cryptocurrencyWallet_service import CryptocurrencyWalletService

wallet_service = CryptocurrencyWalletService()
coin_api_service = COINAPIService()


class CryptocurrencyWalletController:

    @staticmethod
    def list_wallets():
        try:
            wallets = wallet_service.get_all_wallets()
            return jsonify([wallet.to_dict() for wallet in wallets])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_wallet_by_id(wallet_id):
        try:
            wallet = wallet_service.get_wallet_by_id(wallet_id)
            if not wallet:
                raise WalletNotFoundError(wallet_id)
            return jsonify(wallet.to_dict())
        except WalletNotFoundError as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_wallets_by_user(user_id):
        try:
            wallets = wallet_service.get_wallets_by_user(user_id)
            return jsonify([wallet.to_dict() for wallet in wallets])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_wallet_by_user_and_currency(user_id, currency):
        try:
            wallet = wallet_service.get_wallet_by_user_and_currency(user_id, currency)
            if not wallet:
                return jsonify({'error': 'Wallet not found for user and currency'}), 404
            return jsonify(wallet.to_dict())
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def create_wallet(data):
        try:
            if not data or 'user_id' not in data or 'currency' not in data:
                raise ValueError('Missing required fields (user_id, currency)')

            new_wallet = wallet_service.create_wallet(data['user_id'], data['currency'])
            if not new_wallet:
                raise WalletCreationError('Failed to create wallet')

            return jsonify(new_wallet.to_dict()), 201
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except WalletCreationError as wce:
            return jsonify({'error': str(wce)}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_wallet(wallet_id, data):
        try:
            if not data or not wallet_id:
                raise ValueError('Missing data or wallet_id')

            updated_wallet = wallet_service.update_wallet(wallet_id, data)
            if not updated_wallet:
                raise WalletUpdateError('Wallet not found or failed to update')

            return jsonify(updated_wallet.to_dict())
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except WalletUpdateError as wue:
            return jsonify({'error': str(wue)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_wallet(wallet_id):
        try:
            if wallet_service.delete_wallet(wallet_id):
                return jsonify({'message': 'Wallet deleted successfully'})
            else:
                return jsonify({'error': 'Failed to delete wallet'}), 500
        except WalletDeletionError as wde:
            return jsonify({'error': str(wde)}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def calculate_portfolio_value(user_id):
        try:
            wallets = wallet_service.get_wallets_by_user(user_id)
            if not wallets:
                return jsonify({'error': 'User has no wallets or does not exist'}), 404

            return coin_api_service.get_portfolio_value(self=coin_api_service, user_id=user_id)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
