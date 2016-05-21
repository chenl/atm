# -*- coding: utf-8 -*-

import pytest
from atm.menu import Menu

def menu_foo_bar(): pass
def menu_baz(): pass

class MockIO(object):
    def put(self, _):
        pass
    def get_menu_entry(self, _):
        return 2

@pytest.fixture
def some_menu():
    return Menu({'menu':[menu_foo_bar, menu_baz]}, MockIO())


def test_menu_creation():
    menu = Menu('menus', 'io')
    assert menu.menus == 'menus'
    assert menu.io == 'io'

def test_men_screen(some_menu):
    assert some_menu.screen('menu') == """\
Menu
----
1. Foo Bar
2. Baz"""

def test_menu_fn(some_menu):
    assert some_menu.fn('menu') == menu_baz
