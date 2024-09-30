from databases.interfaces import Record

from src.database import database
from src.models.account import accounts
from src.schemas.account import AccountRequest
from datetime import datetime
from src.exceptions import AccountFoundError
from src.models.transaction import TransactionType, transactions


class AccountService:
    async def read_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def create(self, account: AccountRequest) -> Record:

        query = accounts.select().where(accounts.c.user_id == account.user_id)
        account_test = await database.fetch_one(query)

        if account_test:
            raise AccountFoundError("already have an account created for this user!!!")

        # Inclui a conta
        command = accounts.insert().values(
            user_id=account.user_id,
            balance=account.balance,
            timestamp=datetime.now(),
        )
        account_id = await database.execute(command)

        # inclui o depósito
        command = transactions.insert().values(
            account_id=account_id,
            type=TransactionType.DEPOSIT,
            amount=account.balance,
            timestamp=datetime.now(),
        )
        await database.execute(command)

        # Retorna os dados da conta
        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)
