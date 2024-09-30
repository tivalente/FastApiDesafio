from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
