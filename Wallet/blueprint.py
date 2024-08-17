from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from Wallet.Controller.cryptocurrencyWallet_controller import CryptocurrencyWalletController

wallet_bp = Blueprint('wallet', __name__, url_prefix='/wallets')


@wallet_bp.route('/', methods=['GET'])
@jwt_required()
def list_wallets():
    return CryptocurrencyWalletController.list_wallets()


@wallet_bp.route('/<int:wallet_id>', methods=['GET'])
@jwt_required()
def get_wallet(wallet_id):
    return CryptocurrencyWalletController.get_wallet_by_id(wallet_id)


@wallet_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_wallets_by_user(user_id):
    return CryptocurrencyWalletController.get_wallets_by_user(user_id)


@wallet_bp.route('/user/<int:user_id>/<string:currency>', methods=['GET'])
@jwt_required()
def get_wallet_by_user_and_currency(user_id, currency):
    return CryptocurrencyWalletController.get_wallet_by_user_and_currency(user_id, currency)


@wallet_bp.route('/', methods=['POST'])
@jwt_required()
def create_wallet():
    data = request.get_json()
    return CryptocurrencyWalletController.create_wallet(data)


@wallet_bp.route('/<int:wallet_id>', methods=['PUT'])
@jwt_required()
def update_wallet(wallet_id):
    data = request.get_json()
    return CryptocurrencyWalletController.update_wallet(wallet_id,data)


@wallet_bp.route('/<int:wallet_id>', methods=['DELETE'])
@jwt_required()
def delete_wallet(wallet_id):
    return CryptocurrencyWalletController.delete_wallet(wallet_id)
