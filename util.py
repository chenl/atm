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

def indexize(inp, upto):
    """get a selection from a raw input

    If selection is valid an integer (i) between 1 and upto, return (i-1)
    else return None

    Note input is 1-based and the return index is 0-based

    >>> indexize('2', 3)
    1
    >>> indexize('3', 3)
    2
    >>> indexize('1', 1)
    0
    >>> indexize('2', 1)
    None
    >>> indexize('x', 5)
    None
    """
    try:
        i = int(inp) - 1 # menu is 1-base, index is 0-base
    except ValueError:
        return None
    # menu is one base
    if 0 <= i < upto:
        return i
    else:
        return None
