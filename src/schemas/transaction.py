from enum import Enum

from pydantic import BaseModel, PositiveFloat
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"


class TransactionRequest(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat

    class Config:
        use_enum_values = True
