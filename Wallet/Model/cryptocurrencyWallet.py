from sqlalchemy import UniqueConstraint

from db_extension import db


class CryptocurrencyWallet(db.Model):
    __tablename__ = 'cryptocurrency_wallets'
    wallet_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Numeric(20, 8), default=0.00000000)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    transactions = db.relationship('Transaction', backref='wallet', cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('user_id', 'currency', name='uq_user_currency'),
    )
