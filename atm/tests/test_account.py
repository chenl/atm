# -*- coding: utf-8 -*-

import pytest
from atm.account import Account, AccountException

@pytest.fixture
def new_account():
    'a new account with balance of 0'
    return Account('new_account')

@pytest.fixture
def account_100():
    'account with balance of 100'
    return Account('account_100', 100)

def test_account_creation(new_account):
    assert new_account.id == 'new_account'
    assert new_account.balance == 0

def test_account_creation_with_balance(account_100):
    assert account_100.id == 'account_100'
    assert account_100.balance == 100

def test_account_deposit(new_account):
    new_account.deposit(42)
    assert new_account.balance == 42

def test_account_withdraw(account_100):
    account_100.withdraw(25)
    assert account_100.balance == 75

def test_account_withdraw_all_at_once(account_100):
    account_100.withdraw(100)
    assert account_100.balance == 0

def test_account_overdraft(account_100):
    with pytest.raises(AccountException):
        account_100.withdraw(101)
    assert account_100.balance == 100

def test_account_negative_withdraw(account_100):
    with pytest.raises(ValueError):
        account_100.withdraw(-1)

def test_account_negative_deposit(account_100):
    with pytest.raises(ValueError):
        account_100.deposit(-1)
