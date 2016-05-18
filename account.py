#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AccountException(Exception):
    pass

class Account(object):

    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, ammount):
        if ammount > self.balance():
            raise AccountException('overdraft')
        self.balance -= ammount

    def deposit(self, ammount):
        self.balance += ammount

    def check_balance(self):
        return self.balance()

def main():
    pass

if __name__ == '__main__':
    main()
