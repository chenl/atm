#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AccountException(Exception):
    pass

class Account(object):

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.id)

    def withdraw(self, ammount):
        if ammount < 0:
            raise ValueError('negative withdraw')
        if ammount > self.balance:
            raise AccountException('overdraft')
        self.balance -= ammount

    def deposit(self, ammount):
        if ammount < 0:
            raise ValueError('negative deposit')
        self.balance += ammount
