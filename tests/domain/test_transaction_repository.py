from app.adapter.inmemory_transaction_repository import InMemoryTransactionRepository
from app.domain.transaction import Transaction


def test_save_transaction():
    transaction_repository = InMemoryTransactionRepository()

    t1 = Transaction(account_id="accounts/1", operation_type="credit", operation_description="deposito", amount=1000)
    t2 = Transaction(account_id="accounts/1", operation_type="debit", operation_description="saque", amount=100)
    t3 = Transaction(account_id="accounts/2", operation_type="debit", operation_description="saque", amount=200)

    t1.save(transaction_repository)
    t2.save(transaction_repository)
    t3.save(transaction_repository)

    assert len(transaction_repository.transactions) == 3
    assert t2.id == "transactions/2"
