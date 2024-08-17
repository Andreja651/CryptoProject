from db_extension import db


class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Numeric(20, 8), nullable=False)
    transaction_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    __table_args__ = (
        db.ForeignKeyConstraint(['user_id', 'currency'],
                                ['cryptocurrency_wallets.user_id', 'cryptocurrency_wallets.currency'],
                                ondelete='CASCADE'),
        db.CheckConstraint('transaction_type IN (\'buy\', \'sell\')', name='valid_transaction_type')
    )
