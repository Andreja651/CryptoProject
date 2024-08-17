from flask import jsonify

from Exceptions.custom_exceptions import TransactionNotFoundError, DatabaseOperationError, InvalidTransactionDataError
from Transaction.Service.transaction_service import TransactionService

transaction_service = TransactionService()


class TransactionController:
    @staticmethod
    def get_transaction_by_id(transaction_id):
        try:
            transaction = transaction_service.get_transaction_by_id(transaction_id)
            if not transaction:
                return jsonify({'error': 'Transaction not found'}), 404
            return jsonify(transaction.to_dict())
        except TransactionNotFoundError as e:
            return jsonify({'error': str(e)}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500

    @staticmethod
    def get_transactions(data):
        if not data or 'user_id' not in data or 'transaction_type' not in data or 'currency' not in data :
            return jsonify({'error': 'Missing required fields (user_id, transaction_type, currency)'}), 400
        user_id = data['user_id']
        transaction_type = data['transaction_type']
        currency = data['currency']
        try:
            transactions = transaction_service.get_transactions(user_id, currency, transaction_type)
            if not transactions:
                return jsonify({'error': 'Transaction not found'}), 404
            return jsonify(transactions.to_dict())
        except TransactionNotFoundError as e:
            return jsonify({'error': str(e)}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500

    @staticmethod
    def create_transaction(data):
        try:
            if not data or 'user_id' not in data or 'transaction_type' not in data or 'currency' not in data or 'amount' not in data:
                return jsonify({'error': 'Missing required fields (user_id, transaction_type, currency, amount)'}), 400

            new_transaction = transaction_service.create_transaction(data['user_id'], data['transaction_type'],
                                                                     data['currency'], data['amount'])
            if not new_transaction:
                return jsonify({'error': 'Failed to create transaction'}), 500
            return jsonify(new_transaction.to_dict()), 201
        except InvalidTransactionDataError as e:
            return jsonify({'error': str(e)}), 400
        except DatabaseOperationError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500

    @staticmethod
    def update_transaction(transaction_id, data):
        try:
            if not data or 'currency' not in data or 'amount' not in data:
                return jsonify({'error': 'Missing required fields (currency amount)'}), 400
            updated_transaction = transaction_service.update_transaction(transaction_id, data['currency'],
                                                                         data['amount'])
            if not updated_transaction:
                return jsonify({'error': 'Transaction not found or failed to update'}), 404
            return jsonify(updated_transaction.to_dict())
        except TransactionNotFoundError as e:
            return jsonify({'error': str(e)}), 404
        except DatabaseOperationError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500

    @staticmethod
    def delete_transaction(transaction_id):
        try:
            if transaction_service.delete_transaction(transaction_id):
                return jsonify({'message': 'Transaction deleted successfully'})
            return jsonify({'error': 'Failed to delete transaction'}), 500
        except DatabaseOperationError as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500
