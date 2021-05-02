from app.adapter.inmemory_transaction_repository import InMemoryTransactionRepository
from app.domain.transaction import Transaction


def main():
    transaction_repository = InMemoryTransactionRepository()

    t1 = Transaction(account_id="accounts/1", operation_type="credit", operation_description="deposito", amount=1000)
    t2 = Transaction(account_id="accounts/1", operation_type="debit", operation_description="saque", amount=100)
    t3 = Transaction(account_id="accounts/2", operation_type="debit", operation_description="saque", amount=200)

    t1.save(transaction_repository)
    t2.save(transaction_repository)
    t3.save(transaction_repository)

    print(transaction_repository.all())

    print(transaction_repository.account_transactions('accounts/1'))


if __name__ == '__main__':
    main()
