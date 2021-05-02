from abc import ABC
from typing import List

from app.domain.transaction import Transaction
from app.domain.transaction_repository import TransactionRepository


class InMemoryTransactionRepository(TransactionRepository, ABC):
    def __init__(self):
        self.transactions = []

    def add(self, transaction: Transaction) -> Transaction:
        next_id = len(self.transactions)+1
        transaction.id = f'transactions/{next_id}'
        self.transactions.append(transaction)
        return transaction

    def all(self) -> List[Transaction]:
        return self.transactions

    def account_transactions(self, account_id: str) -> List[Transaction]:
        return [x for x in self.transactions if x.account_id == account_id]


