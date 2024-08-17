

class CryptocurrencyWalletDTO:
    def __init__(self, wallet_id, user_id, currency, balance, created_at):
        self.wallet_id = wallet_id
        self.user_id = user_id
        self.currency = currency
        self.balance = balance
        self.created_at = created_at

    @staticmethod
    def from_model(wallet):
        return CryptocurrencyWalletDTO(
            wallet_id=wallet.wallet_id,
            user_id=wallet.user_id,
            currency=wallet.currency,
            balance=wallet.balance,
            created_at=wallet.created_at,
        )

    def to_dict(self):
        return {
            'wallet_id': self.wallet_id,
            'user_id': self.user_id,
            'currency': self.currency,
            'balance': float(self.balance),
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
