#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atm.store import Store
from atm.bank import Bank
from atm.ui import bank_menu

def main():
    with Bank(Store('bank.csv')) as bank:
        bank_menu(bank)

if __name__ == '__main__':
    main()
