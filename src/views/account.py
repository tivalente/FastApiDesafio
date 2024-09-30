from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
