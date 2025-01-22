import pytest

from bank import Account

@pytest.fixture
def account():
    return Account(initial_balance=1000)

def test_deposit(account):
    account.deposit(1000)
    assert account.balance == 2000

def test_withdraw(account):
    account.withdraw(500)
    assert account.balance == 500

def test__create_identifier_length_of_identifier(account):
    assert len(account.identifier) == 25
    assert account.identifier.isalnum() is True

def test__create_identifier_is_all_alnum(account):
    assert account.identifier.isalnum() is True