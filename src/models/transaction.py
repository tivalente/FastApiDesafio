import sqlalchemy as sa
from src.database import metadata
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column(
        "account_id",
        sa.Integer,
        sa.ForeignKey("accounts.id"),
        nullable=False,
        index=True,
    ),
    sa.Column(
        "type", sa.Enum(TransactionType, name="transaction_types"), nullable=False
    ),
    sa.Column("timestamp", sa.TIMESTAMP(timezone=True), nullable=True),
)
