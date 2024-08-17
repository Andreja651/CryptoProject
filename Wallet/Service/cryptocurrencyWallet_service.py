from Exceptions.custom_exceptions import WalletDeletionError, WalletNotFoundError, DatabaseOperationError, WalletUpdateError, \
    WalletCreationError
from Wallet.Model.cryptocurrencyWallet import CryptocurrencyWallet
from Wallet.Repository.cryptocurrencyWallet_repository import CryptocurrencyWalletRepository
from Wallet.DTO.cryptocurrencyWallet_dto import CryptocurrencyWalletDTO
from datetime import datetime


class CryptocurrencyWalletService:

    @staticmethod
    def get_wallet_by_id(wallet_id):
        """
        Gets The wallet by ID
        :param wallet_id: The ID for the Wallet
        :return: The Wallet Mapped to DTO
        """
        try:
            wallet = CryptocurrencyWalletRepository.get_by_id(wallet_id)
            if not wallet:
                raise WalletNotFoundError(f"Wallet with ID {wallet_id} not found.")
            return CryptocurrencyWalletDTO.from_model(wallet)
        except WalletNotFoundError as e:
            print(f"Wallet not found error: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Repository error in get_wallet_by_id: {e}")
            return None
        except Exception as e:
            print(f"Error in get_wallet_by_id: {e}")
            return None

    @staticmethod
    def get_all_wallets():
        """
        Gets All wallets in the Database
        :return: List of Wallets Mapped DTO
        """
        try:
            wallets = CryptocurrencyWalletRepository.get_all_wallets()
            return [CryptocurrencyWalletDTO.from_model(wallet) for wallet in wallets]
        except DatabaseOperationError as e:
            print(f"Repository error in get_all_wallets: {e}")
            return []
        except Exception as e:
            print(f"Error in get_all_wallets: {e}")
            return []

    @staticmethod
    def get_wallet_by_user_and_currency(user_id, currency):
        """
        Get Wallet by User and Currency
        :param user_id: The Id of the User
        :param currency: The Currency of the Waller
        :return: The Wallet Mapped to DTO
        """
        try:
            wallet = CryptocurrencyWalletRepository.get_by_user_and_currency(user_id, currency)
            if not wallet:
                raise WalletNotFoundError(f"Wallet for user {user_id} with currency {currency} not found.")
            return CryptocurrencyWalletDTO.from_model(wallet)
        except WalletNotFoundError as e:
            print(f"Wallet not found error: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Repository error in get_wallet_by_user_and_currency: {e}")
            return None
        except Exception as e:
            print(f"Error in get_wallet_by_user_and_currency: {e}")
            return None

    @staticmethod
    def get_wallets_by_user(user_id):
        """
        Get All wallets by User
        :param user_id: ID of the User
        :return: List of Wallets Mapped to DTO
        """
        try:
            wallets = CryptocurrencyWalletRepository.get_all_by_user(user_id)
            return [CryptocurrencyWalletDTO.from_model(wallet) for wallet in wallets]
        except DatabaseOperationError as e:
            print(f"Repository error in get_wallets_by_user: {e}")
            return []
        except Exception as e:
            print(f"Error in get_wallets_by_user: {e}")
            return []

    @staticmethod
    def create_wallet(user_id, currency):
        """
        Create the Wallet
        :param user_id: The Id of the User linked
        :param currency: The Currency for the Wallet
        :return: The created Wallet Mapped to DTO
        """
        try:
            new_wallet = CryptocurrencyWallet(user_id=user_id, currency=currency, created_at=datetime.now())
            created_wallet = CryptocurrencyWalletRepository.create(new_wallet)
            if not created_wallet:
                raise WalletCreationError("Failed to create wallet.")
            return CryptocurrencyWalletDTO.from_model(created_wallet)
        except WalletCreationError as e:
            print(f"Wallet creation error: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Repository error in create_wallet: {e}")
            return None
        except Exception as e:
            print(f"Error in create_wallet: {e}")
            return None

    @staticmethod
    def update_wallet(wallet_id, data):
        """
        Updates the Wallet
        :param wallet_id: The ID of the Wallet to Update
        :param data: The Data passed from the request
        :return: The Updated Wallet Mapped to DTO
        """
        try:
            wallet = CryptocurrencyWalletRepository.get_by_id(wallet_id)
            if not wallet:
                raise WalletNotFoundError(f"Wallet with ID {wallet_id} not found.")

            for key, value in data.items():
                setattr(wallet, key, value)

            updated_wallet = CryptocurrencyWalletRepository.update(wallet)
            if not updated_wallet:
                raise WalletUpdateError("Failed to update wallet.")

            return CryptocurrencyWalletDTO.from_model(updated_wallet)
        except WalletNotFoundError as e:
            print(f"Wallet not found error: {e}")
            return None
        except WalletUpdateError as e:
            print(f"Wallet update error: {e}")
            return None
        except DatabaseOperationError as e:
            print(f"Repository error in update_wallet: {e}")
            return None
        except Exception as e:
            print(f"Error in update_wallet: {e}")
            return None

    @staticmethod
    def delete_wallet(wallet_id):
        """
        Deletes the Wallet
        :param wallet_id: The ID of the Wallet to Delete
        :return: The ID of the deleted Wallet
        """
        try:
            wallet = CryptocurrencyWalletRepository.get_by_id(wallet_id)
            if not wallet:
                raise WalletNotFoundError(f"Wallet with ID {wallet_id} not found.")

            deleted_wallet = CryptocurrencyWalletRepository.delete(wallet)
            if not deleted_wallet:
                raise WalletDeletionError("Failed to delete wallet.")

            return deleted_wallet
        except WalletNotFoundError as e:
            print(f"Wallet not found error: {e}")
            return False
        except WalletDeletionError as e:
            print(f"Wallet deletion error: {e}")
            return False
        except DatabaseOperationError as e:
            print(f"Repository error in delete_wallet: {e}")
            return False
        except Exception as e:
            print(f"Error in delete_wallet: {e}")
            return False

    @staticmethod
    def update_wallet_balance(transaction):
        """
        Updates the Wallet Balance when a Transaction is Created or Updated
        :param transaction: The Updated Transaction
        """
        wallet = CryptocurrencyWalletRepository.get_by_user_and_currency(transaction.user_id, transaction.currency)
        if wallet:
            if transaction.transaction_type == 'purchase':
                wallet.balance += transaction.amount
            elif transaction.transaction_type == 'sell':
                wallet.balance -= transaction.amount

        CryptocurrencyWalletRepository.update(wallet)
