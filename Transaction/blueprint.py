from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from Transaction.Controller.transaction_controller import TransactionController

transaction_bp = Blueprint('transaction', __name__, url_prefix='/transactions')


@transaction_bp.route('/<int:transaction_id>', methods=['GET'])
@jwt_required()
def get_transaction(transaction_id):
    return TransactionController.get_transaction_by_id(transaction_id)


@transaction_bp.route('/', methods=['GET'])
@jwt_required()
def get_transactions():
    data = request.get_json()
    return TransactionController.get_transactions(data)


@transaction_bp.route('/', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    return TransactionController.create_transaction(data)


@transaction_bp.route('/<int:transaction_id>', methods=['PUT'])
@jwt_required()
def update_transaction(transaction_id):
    data = request.get_json()
    return TransactionController.update_transaction(transaction_id, data)


@transaction_bp.route('/<int:transaction_id>', methods=['DELETE'])
@jwt_required()
def delete_transaction(transaction_id):
    return TransactionController.delete_transaction(transaction_id)
