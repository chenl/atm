# -*- coding: utf-8 -*-

def put(msg):
    print msg

def pause(msg='[Enter] -- contunue'):
    raw_input(msg)

def err(msg):
    print 'Error: %s' % msg
    pause()

def get(msg=''):
    return raw_input(msg)

def get_int(msg='', err_msg='Not an integer'):
    while True:
        try:
            return int(get(msg))
        except ValueError:
            err(err_msg)

def get_amount(msg='', err_msg='Negative amount'):
    while True:
        amount = get_int(msg)
        if amount >= 0:
            return amount
        err(err_msg)

def get_menu_entry(max_val, msg=''):
    err_msg = 'must be between 1 and %d' % max_val
    while True:
        val = get_int(msg, err_msg)
        if 1 <= val <= max_val:
            return val
        err(err_msg)

def get_password(msg):
    return get(msg)
