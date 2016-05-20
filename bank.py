#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import atm.account

class Bank(object):

    def __init__(self):
        self.accounts = {}

    def load(self, file):
        pass

    def save(self, file):
        pass

    def account(self, id):
        try:
            return self.accounts[id]
        except IndexError:
            raise account.AccountException('not exists')
