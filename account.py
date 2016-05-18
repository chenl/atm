#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AccountException(Exception):
    pass

class Account(object):

    def __init__(self, id):
        self.id = id
        self.balance = 0

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.id)

    def withdraw(self, ammount):
        if ammount > self.balance:
            raise AccountException('overdraft')
        self.balance -= ammount

    def deposit(self, ammount):
        self.balance += ammount
