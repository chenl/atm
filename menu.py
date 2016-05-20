# -*- coding: utf-8 -*-

class Menu(object):

    def __init__(self, menus, io):
        self.menus = menus

    def fn(self, name):
        menu = self.menus[name]
        self.io.put(screen(name))
        return menu[self.io.get_menu_entry(len(menu)) - 1]

    def screen(self, name):
        """return menu screen for MENUS[name]

        >>> def menu_foo(): pass
        >>> def menu_bar(): pass
        >>> m = Menu({'menu':[menu_foo,menu_bar]}, atm.io)
        >>> m.screen('menu')
        Menu
        ----
        1. Foo
        2. Bar

        """

        lines = [name.title(), '-'*len(name)]
        lines.extend(['%d. %s' % (k, fn_to_title(fn))
                      for key,fn in enumerate(MENUS[name],1)])
        return '\n'.join(lines)
