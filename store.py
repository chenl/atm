# -*- coding: utf-8 -*-

"""Account data storage"""

import atm.store
import atm.account

class Bank(object):
    def __init__(self, store):
        self.store = store
        self.accounts = {}

    def load(self):
        self.accounts = self.store.load()

    def save(self):
        self.store.save(self.accounts)

    def get_account(self, id):
        return self.accounts[id]

    def put_account(self, account):
        self.accounts[account.id] = account
