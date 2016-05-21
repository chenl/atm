# -*- coding: utf-8 -*-

import pytest
from atm.bank import Bank, BankException
from atm.account import Account

LIST_CONTENT = [('new_account', 0), ('account_100', 100)]
DICT_CONTENT = { 'new_account': 0, 'account_100': 100 }

class MockStore(object):
    def __iter__(self):
        return iter(LIST_CONTENT)
    def __call__(self, it):
        self.saved = list(it)

@pytest.fixture
def some_bank():
    return Bank(MockStore())

@pytest.fixture
def loaded_bank(some_bank):
    some_bank.load()
    return some_bank


def test_bank_creation():
    bank = Bank('store')
    assert bank.store == 'store'
    assert bank.accounts == {}

def test_bank_load(some_bank):
    some_bank.load()
    assert some_bank.accounts == DICT_CONTENT

def test_bank_save(some_bank):
    some_bank.accounts = DICT_CONTENT
    some_bank.save()
    assert some_bank.store.saved == LIST_CONTENT

def test_bank_load_save(loaded_bank):
    loaded_bank.save()
    assert loaded_bank.store.saved == LIST_CONTENT

def test_bank_context(some_bank):
    with some_bank:
       assert some_bank.accounts == DICT_CONTENT
    assert some_bank.store.saved == LIST_CONTENT

def test_get_account(loaded_bank):
    account = loaded_bank.get_account('account_100')
    assert account.id == 'account_100'
    assert account.balance == 100

def test_get_account_exception(loaded_bank):
    with pytest.raises(BankException):
        loaded_bank.get_account('non_exist_account')

def test_put_account(loaded_bank):
    account = Account('non_exists_account', 42)
    loaded_bank.put_account(account)
    assert loaded_bank.accounts['non_exists_account'] == 42

def test_assert_put_get(loaded_bank):
    put_acc = Account('non_exists_account', 42)
    loaded_bank.put_account(put_acc)
    get_acc = loaded_bank.get_account('non_exists_account')
    assert get_acc.id == 'non_exists_account'
    assert get_acc.balance == 42
