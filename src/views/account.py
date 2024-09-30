from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat
from datetime import datetime


class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    timestamp: datetime


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
