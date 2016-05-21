#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .account import Account

class BankException(Exception):
    pass

class Bank(object):

    def __init__(self, store):
        self.store = store
        self.accounts = {}

    def load(self):
        self.accounts = {id:int(balance) for id,balance in self.store}

    def save(self):
        self.store(self.accounts.iteritems())

    def __enter__(self):
        self.load()

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()

    def get_account(self, id):
        try:
            return Account(id, self.accounts[id])
        except KeyError:
            raise BankException('not exists', id)

    def put_account(self, account):
        self.accounts[account.id] = account.balance
