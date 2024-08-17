"""add CryptoCyrrencyWallet

Revision ID: 82afa3592b3d
Revises: 71e96cd54c32
Create Date: 2024-06-30 12:19:02.945915

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '82afa3592b3d'
down_revision = '71e96cd54c32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('transaction_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('transaction_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('currency', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('amount', sa.NUMERIC(precision=20, scale=8), autoincrement=False, nullable=False),
    sa.Column('transaction_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id', 'currency'], ['cryptocurrency_wallets.user_id', 'cryptocurrency_wallets.currency'], name='transactions_user_id_currency_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='transactions_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('transaction_id', name='transactions_pkey')
    )
    # ### end Alembic commands ###
