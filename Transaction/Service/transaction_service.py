from Exceptions.custom_exceptions import TransactionServiceError, TransactionCreationError, TransactionUpdateError, \
    TransactionDeletionError
from Transaction.Repository.transaction_repository import TransactionRepository
from Transaction.DTO.transaction_dto import TransactionDTO
from Transaction.Model.transaction import Transaction
from Wallet.Service.cryptocurrencyWallet_service import CryptocurrencyWalletService


class TransactionService:
    @staticmethod
    def get_transaction_by_id(transaction_id):
        """
        Get the Transaction by ID
        :param transaction_id: transaction ID
        :return: Mapped Transaction to DTO
        """
        try:
            transaction = TransactionRepository.get_by_id(transaction_id)
            if transaction:
                return TransactionDTO.from_model(transaction)
            return None
        except Exception as e:
            raise TransactionServiceError(f"Error in get_transaction_by_id: {e}")

    @staticmethod
    def get_transactions(user_id, currency, transaction_type):
        """
       Get the Transaction by ID
       :param user_id: User Authenticated ID
       :param currency: Currency for filter transactions
       :param transaction_type:  Transaction type for filter
       :return: Mapped Transaction to DTO list
       """
        try:
            transactions = TransactionRepository.get_transactions(user_id, currency, transaction_type)
            if transactions:
                return [TransactionDTO.from_model(transaction) for transaction in transactions]
            return None
        except Exception as e:
            raise TransactionServiceError(f"Error in get_transaction_by_id: {e}")

    @staticmethod
    def create_transaction(user_id, transaction_type, currency, amount):
        """
`       Creates a Transaction
        :param user_id: The User creating the Transaction
        :param transaction_type: The type of the transaction(purchase,sell)
        :param currency: The Currency Value of the Transaction
        :param amount: The Amount for the Transaction
        :return: The Transaction Created Mapped to DTO
        """
        try:
            new_transaction = Transaction(
                user_id=user_id,
                transaction_type=transaction_type,
                currency=currency,
                amount=amount
            )
            TransactionRepository.create(new_transaction)
            CryptocurrencyWalletService.update_wallet_balance(new_transaction)
            return TransactionDTO.from_model(new_transaction)
        except Exception as e:
            raise TransactionCreationError(f"Error in create_transaction: {e}")

    @staticmethod
    def update_transaction(transaction_id, currency, amount):
        """
        Updates The Transaction
        :param transaction_id: The Id for the transaction to Update
        :param currency: The currency to Update with
        :param amount: The amount to update with
        :return: The Updated Transaction mapped to DTO
        """
        try:
            transaction = TransactionRepository.get_by_id(transaction_id)

            if transaction:
                transaction_to_update = transaction
                transaction_to_update.currency = currency
                transaction_to_update.amount = amount
                updated_transaction = TransactionRepository.update(transaction_to_update)
                CryptocurrencyWalletService.update_wallet_balance(updated_transaction)
                return TransactionDTO.from_model(updated_transaction)
            else:
                return None
        except Exception as e:
            raise TransactionUpdateError(f"Error in update_transaction: {e}")

    @staticmethod
    def delete_transaction(transaction_id):
        """
        Deletes the Transaction
        :param transaction_id: The Id of the Transaction to delete
        :return: boolean
        """
        try:
            transaction = TransactionRepository.get_by_id(transaction_id)
            if not transaction:
                return False
            TransactionRepository.delete(transaction)
            return True
        except Exception as e:
            raise TransactionDeletionError(f"Error in delete_transaction: {e}")
