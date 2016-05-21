# -*- coding: utf-8 -*-

def remove_up_to(sub, string):
    """Remove everything from the beginning of string up to (and
    including) the end of the first occerance of sub-string

    >>> remove_up_to('_', 'abc_def_ghj')
    'def_ghj'

    """
    return string[string.find(sub)+len(sub):]


def fn_to_title(fn):
    """make a title out of a the name of a menu function

    >>> fn_to_title(fn_to_title)
    'To Title'

    """
    return remove_up_to('_', fn.func_name).replace('_', ' ').title()
