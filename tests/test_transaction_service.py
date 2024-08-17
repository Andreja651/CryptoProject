import unittest
from unittest.mock import patch

from Transaction.Model.transaction import Transaction
from Transaction.Service.transaction_service import TransactionService


class TestTransactionService(unittest.TestCase):

    @patch('Transaction.Repository.transaction_repository.TransactionRepository')
    def test_get_transaction_by_id(self, MockTransactionRepository):
        mock_transaction = Transaction(transaction_id=1, user_id=1, transaction_type='deposit', currency='BTC',
                                       amount=1.0)
        MockTransactionRepository.get_by_id.return_value = mock_transaction

        transaction_id = 1
        result = TransactionService.get_transaction_by_id(transaction_id)

        self.assertEqual(result.transaction_id, mock_transaction.transaction_id)
        MockTransactionRepository.get_by_id.assert_called_once_with(transaction_id)

    @patch('Transaction.Repository.transaction_repository.TransactionRepository')
    def test_create_transaction(self, MockTransactionRepository):
        user_id = 1
        transaction_type = 'deposit'
        currency = 'BTC'
        amount = 1.0

        mock_transaction = Transaction(transaction_id=1, user_id=user_id, transaction_type=transaction_type,
                                       currency=currency, amount=amount)
        MockTransactionRepository.create.return_value = mock_transaction

        result = TransactionService.create_transaction(user_id, transaction_type, currency, amount)

        self.assertEqual(result.user_id, user_id)
        self.assertEqual(result.currency, currency)
        MockTransactionRepository.create.assert_called_once()

    @patch('Transaction.Repository.transaction_repository.TransactionRepository')
    def test_update_transaction(self, MockTransactionRepository):
        mock_transaction = Transaction(transaction_id=1, user_id=1, transaction_type='deposit', currency='BTC',
                                       amount=1.0)
        MockTransactionRepository.update.return_value = mock_transaction

        result = TransactionService.update_transaction(mock_transaction.transaction_id, 'ETH', 'ETH', 2.0)

        self.assertEqual(result.transaction_id, mock_transaction.transaction_id)
        self.assertEqual(result.currency, 'ETH')
        self.assertEqual(result.amount, 2.0)
        MockTransactionRepository.update.assert_called_once_with(mock_transaction)

    @patch('Transaction.Repository.transaction_repository.TransactionRepository')
    def test_delete_transaction(self, MockTransactionRepository):
        mock_transaction = Transaction(transaction_id=1, user_id=1, transaction_type='deposit', currency='BTC',
                                       amount=1.0)

        result = TransactionService.delete_transaction(mock_transaction.transaction_id)

        self.assertTrue(result)
        MockTransactionRepository.delete.assert_called_once_with(mock_transaction)


if __name__ == '__main__':
    unittest.main()
