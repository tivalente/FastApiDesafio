from fastapi import APIRouter, Depends, status

from src.schemas.transaction import TransactionRequest
from src.security import login_required
from src.services.transaction import TransactionService
from src.views.transaction import TransactionResponse

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])
# router = APIRouter(prefix="/transactions")

service = TransactionService()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=TransactionResponse
)
async def create_transaction(transaction: TransactionRequest):
    return await service.create(transaction)
