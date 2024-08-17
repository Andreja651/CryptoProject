class TransactionNotFoundError(Exception):
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.message = f"Transaction with ID {transaction_id} not found."
        super().__init__(self.message)


class DatabaseOperationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TransactionServiceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TransactionCreationError(TransactionServiceError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TransactionUpdateError(TransactionServiceError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TransactionDeletionError(TransactionServiceError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class RepositoryError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UserNotFoundError(RepositoryError):
    def __init__(self, user_id):
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found."
        super().__init__(self.message)


class WalletNotFoundError(Exception):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id
        self.message = f"Wallet with ID {wallet_id} not found."
        super().__init__(self.message)


class WalletCreationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WalletUpdateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WalletDeletionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidTransactionDataError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
