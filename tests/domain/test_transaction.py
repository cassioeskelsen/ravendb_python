from datetime import datetime

from app.domain.transaction import Transaction


def test_transaction_fields():
    t1 = Transaction(account_id="accounts/1", operation_type="credit", operation_description="deposito", amount=1000)
    assert t1.account_id == "accounts/1"
    assert t1.operation_type == "credit"
    assert t1.operation_description == "deposito"
    assert t1.amount == 1000
    assert t1.id is None
    assert t1.date <= datetime.utcnow()
