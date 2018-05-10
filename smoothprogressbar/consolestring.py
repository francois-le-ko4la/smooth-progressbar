#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


class ConsoleString(str):
    """
    Console string is a string to print (stdout) with
    fixed size and console code
    The console code is not calsulate in 'max_size'.

    Why:
        It's usefull to manage the screen size.

    Use:
        >>> c = ConsoleString("lorem ipsum")
        >>> # console code:
        >>> c.tag_beg = "["
        >>> c.tag_end="]"
        >>> for i in range(15): c.max_size = i ; str(c)
        '[]'
        '[l]'
        '[lo]'
        '[lor]'
        '[lore]'
        '[lorem]'
        '[lorem ]'
        '[lorem i]'
        '[lorem ip]'
        '[lorem ips]'
        '[lorem ipsu]'
        '[lorem ipsum]'
        '[lorem ipsum] '
        '[lorem ipsum]  '
        '[lorem ipsum]   '
        >>> len(c)
        11
        >>> c.text
        'lorem ipsum'
        >>> c = ConsoleString("lorem")
        >>> for i in range(9): c.max_size = i ; str(c)
        ''
        'l'
        'lo'
        'lor'
        'lore'
        'lorem'
        'lorem '
        'lorem  '
        'lorem   '
        >>> c = ConsoleString("lorem", ConsoleString.align_right)
        >>> for i in range(9): c.max_size = i ; str(c)
        ''
        'l'
        'lo'
        'lor'
        'lore'
        'lorem'
        ' lorem'
        '  lorem'
        '   lorem'
    """
    def __new__(cls, txt, *args, **kw):
        return str.__new__(cls, txt)

    def __init__(self, txt, frmt=None):
        if frmt is None:
            frmt = ConsoleString.align_left
        self.__max_size = 0
        self.tag_beg = ""
        self.tag_end = ""
        self.__frmt = frmt(self)

    @property
    def text(self):
        return super().__str__()

    @property
    def max_size(self):
        return self.__max_size

    @max_size.setter
    def max_size(self, max_size):
        self.__max_size = max_size

    def align_left(self):
        return "{0}{1}{2}{3}"

    def align_right(self):
        return "{0}{3}{1}{2}"

    def __repr__(self):
        if len(self.text) >= self.__max_size + 1:
            txt = self.tag_beg + self[0:(self.__max_size)] + self.tag_end
        else:
            txt = self.text
            txt = self.__frmt.format(self.tag_beg,
                                     txt,
                                     self.tag_end,
                                     " " * (self.__max_size - len(txt))
                                     )
        return txt

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
