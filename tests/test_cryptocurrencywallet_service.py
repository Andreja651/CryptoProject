import unittest
from datetime import datetime
from unittest.mock import patch

from Wallet.Model.cryptocurrencyWallet import CryptocurrencyWallet
from Wallet.Service.cryptocurrencyWallet_service import CryptocurrencyWalletService


class TestCryptocurrencyWalletService(unittest.TestCase):
    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_get_wallet_by_id(self, MockCryptocurrencyWalletRepository):
        mock_wallet = CryptocurrencyWallet(wallet_id=1, user_id=1, currency='BTC', balance=0.0,
                                           created_at=datetime.now())
        MockCryptocurrencyWalletRepository.get_by_id.return_value = mock_wallet

        wallet_id = 1
        result = CryptocurrencyWalletService.get_wallet_by_id(wallet_id)

        self.assertEqual(result.wallet_id, mock_wallet.wallet_id)
        MockCryptocurrencyWalletRepository.get_by_id.assert_called_once_with(wallet_id)

    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_get_all_wallets(self, MockCryptocurrencyWalletRepository):
        mock_wallet1 = CryptocurrencyWallet(wallet_id=1, user_id=1, currency='BTC', balance=0.0,
                                            created_at=datetime.now())
        mock_wallet2 = CryptocurrencyWallet(wallet_id=2, user_id=2, currency='ETH', balance=0.0,
                                            created_at=datetime.now())
        MockCryptocurrencyWalletRepository.get_all_wallets.return_value = [mock_wallet1, mock_wallet2]

        result = CryptocurrencyWalletService.get_all_wallets()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].wallet_id, mock_wallet1.wallet_id)
        self.assertEqual(result[1].currency, mock_wallet2.currency)
        MockCryptocurrencyWalletRepository.get_all_wallets.assert_called_once()

    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_get_wallet_by_user_and_currency(self, MockCryptocurrencyWalletRepository):

        mock_wallet = CryptocurrencyWallet(wallet_id=1, user_id=1, currency='BTC', balance=0.0,
                                           created_at=datetime.now())
        MockCryptocurrencyWalletRepository.get_by_user_and_currency.return_value = mock_wallet

        user_id = 1
        currency = 'BTC'
        result = CryptocurrencyWalletService.get_wallet_by_user_and_currency(user_id, currency)

        self.assertEqual(result.wallet_id, mock_wallet.wallet_id)
        MockCryptocurrencyWalletRepository.get_by_user_and_currency.assert_called_once_with(user_id, currency)

    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_get_wallets_by_user(self, MockCryptocurrencyWalletRepository):
        mock_wallet1 = CryptocurrencyWallet(wallet_id=1, user_id=1, currency='BTC', balance=0.0,
                                            created_at=datetime.now())
        mock_wallet2 = CryptocurrencyWallet(wallet_id=2, user_id=1, currency='ETH', balance=0.0,
                                            created_at=datetime.now())
        MockCryptocurrencyWalletRepository.get_all_by_user.return_value = [mock_wallet1, mock_wallet2]

        user_id = 1
        result = CryptocurrencyWalletService.get_wallets_by_user(user_id)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].wallet_id, mock_wallet1.wallet_id)
        self.assertEqual(result[1].currency, mock_wallet2.currency)
        MockCryptocurrencyWalletRepository.get_all_by_user.assert_called_once_with(user_id)

    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_create_wallet(self, MockCryptocurrencyWalletRepository):
        user_id = 1
        currency = 'BTC'

        mock_wallet = CryptocurrencyWallet(wallet_id=1, user_id=user_id, currency=currency, balance=0.0,
                                           created_at=datetime.now())
        MockCryptocurrencyWalletRepository.create.return_value = mock_wallet

        result = CryptocurrencyWalletService.create_wallet(user_id, currency)

        self.assertEqual(result.user_id, user_id)
        self.assertEqual(result.currency, currency)
        MockCryptocurrencyWalletRepository.create.assert_called_once()

    @patch('Wallet.Repository.cryptocurrencyWallet_repository.CryptocurrencyWalletRepository')
    def test_update_wallet(self, MockCryptocurrencyWalletRepository):
        mock_wallet = CryptocurrencyWallet(wallet_id=1, user_id=1, currency='BTC', balance=0.0,
                                           created_at=datetime.now())
        MockCryptocurrencyWalletRepository.update.return_value = mock_wallet


