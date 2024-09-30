import sqlalchemy as sa
from src.database import metadata
from enum import Enum
from datetime import datetime


class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"


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
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column(
        "timestamp", sa.TIMESTAMP(timezone=True), nullable=True, default=datetime.now()
    ),
)
