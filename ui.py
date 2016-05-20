# -*- coding: utf-8 -*-

import atm.io
import atm.menu
from atm.util import fn_to_title
from atm.account import Account, AccountException

menu = atm.menu.Menu(
    menus=dict(welcome=[welcome_login, welcome_quit],
               account=[account_check_balance, account_deposit,
                        account_withdraw, account_logoff]),
    io=atm.io)

def welcome_menu():
    while menu.fn('welcome')():
        pass

def welcome_login():
    msg = """\
Login
-----
Please enter your password: """)
    password = atm.io.get(msg)
    try:
        account = get_account(password)
        account_menu(account)
    except:
        print 'Error'
        raw_input("[Enter] -- continue")
    return True

def welcome_quit():
    msg = """\
              _ _   __
Thank you,   ( | ) /_/
          __( >o< )
          \_\(_|_)   Goodbye!

"""
    atm.io.put(msg)
    return False

def account_menu(account):
    while menu.fn('account')(account):
        pass

def account_check_balance(account):
    atm.io.put("Your balance is: %d" % account.balance)
    atm.io.pause()
    return True

def account_deposit(account):
    account.deposit(atm.io.get_amount('Deposit: '))
    return True

def account_withdraw(account):
    try:
        account.withdraw(atm.io.get_ammount('Deposit: '))
    except AccountException:
        atm.io.err('Overdraft!')
    return True

def account_logoff(account):
    save_account(account)
    return False

def main():
    welcome_menu()
