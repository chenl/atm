#!/usr/bin/env python
# -*- coding: utf-8 -*-

from store import Store
from bank import Bank
from ui import bank_menu

def main():
    with Bank(Store('bank.csv')) as bank:
        bank_menu(bank)

if __name__ == '__main__':
    main()
