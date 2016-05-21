# -*- coding: utf-8 -*-

from util import fn_to_title

class Menu(object):

    def __init__(self, menus, io):
        self.menus = menus
        self.io = io

    def screen(self, name):
        "return menu screen for self.menus[name]"
        lines = [name.title(), '-'*len(name)]
        lines.extend(['%d. %s' % (key, fn_to_title(fn))
                      for key,fn in enumerate(self.menus[name],1)])
        return '\n'.join(lines)

    def fn(self, name):
        menu = self.menus[name]
        self.io.put(self.screen(name))
        return menu[self.io.get_menu_entry(len(menu)) - 1]
