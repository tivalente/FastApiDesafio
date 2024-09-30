import sqlalchemy as sa

from src.database import metadata

accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, nullable=False, index=True),
    sa.Column("balance", sa.Numeric(18, 2), nullable=False, default=0),
    sa.Column("timestamp", sa.TIMESTAMP(timezone=True), nullable=True),
)
