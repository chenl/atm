# -*- coding: utf-8 -*-

import io
from menu import Menu
from account import AccountException
from bank import BankException

def bank_login(bank):
    msg = """\
Login
-----
Please enter your password: """
    password = io.get_password(msg)
    try:
        account = bank.get_account(password)
        account_menu(account)
        bank.put_account(account)
    except BankException as ex:
        io.err(ex)
    return True

def bank_quit(bank):
    msg = """\
      _
   _.;_'-._
  {`--.-'_,}
 {; \\,__.-'/}
 {.'-`._;-';
  `'--._.-'
     .-\\\\,-"-.
     `- \\( '-. \\
         \\;---,/
     .-""-;\\
    /  .-' )\\
    \,---'` \\\\ Thank you
             \\| Goodbey!
"""
    io.put(msg)
    return False


def account_check_balance(account):
    io.put("Your balance is: %d" % account.balance)
    io.pause()
    return True

def account_deposit(account):
    account.deposit(io.get_amount('Deposit: '))
    return True

def account_withdraw(account):
    try:
        account.withdraw(io.get_amount('Withdraw: '))
    except AccountException as ex:
        io.err(ex)
    return True

def account_logoff(account):
    return False


MENU = Menu(
    menus=dict(welcome=[bank_login, bank_quit],
               account=[account_check_balance, account_deposit,
                        account_withdraw, account_logoff]),
    io=io)

def bank_menu(bank):
    while MENU.fn('welcome')(bank):
        pass

def account_menu(account):
    while MENU.fn('account')(account):
        pass
