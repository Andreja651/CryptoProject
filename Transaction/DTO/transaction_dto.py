

class TransactionDTO:
    def __init__(self, transaction_id, user_id, transaction_type, currency, amount, transaction_date):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.currency = currency
        self.amount = amount
        self.transaction_date = transaction_date

    @staticmethod
    def from_model( transaction):
        return TransactionDTO(
            transaction_id=transaction.transaction_id,
            user_id=transaction.user_id,
            transaction_type=transaction.transaction_type,
            currency=transaction.currency,
            amount=transaction.amount,
            transaction_date=transaction.transaction_date
        )

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'transaction_type': self.transaction_type,
            'currency': self.currency,
            'amount': str(self.amount),
            'transaction_date': self.transaction_date.isoformat() if self.transaction_date else None
        }
