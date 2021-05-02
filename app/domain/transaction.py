from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.transaction_repository import TransactionRepository


@dataclass
class Transaction:
    account_id: str
    operation_type: str  # credit/debit
    operation_description: str
    amount: float
    id: str = None
    date: datetime = datetime.utcnow()

    def save(self, transaction_repository: 'TransactionRepository'):
        return transaction_repository.add(self)

    def __hash__(self):
        return hash(self.id)
