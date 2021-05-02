import abc
from typing import List

from app.domain.transaction import Transaction


class TransactionRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, transaction: Transaction) -> Transaction:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Transaction]:
        raise NotImplementedError

    @abc.abstractmethod
    def account_transactions(self, account_id: str) -> List[Transaction]:
        raise NotImplementedError
