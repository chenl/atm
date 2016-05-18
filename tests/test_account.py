#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atm.account import Account

def test_account_creation():
    account = Account('id123')
    assert account.id == 'id123'
    assert account.balance == 0
