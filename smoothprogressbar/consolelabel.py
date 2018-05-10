#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from smoothprogressbar.consolestring import ConsoleString


class ConsoleLabel(ConsoleString):
    """

    Why:
        It's usefull to manage the screen size.

    Use:
        >>> c = ConsoleLabel("lorem ipsum dolor")
        >>> str(c)
        'lorem ipsum dolor'
        >>> c.max_size = 5
        >>> print(c.max_size)
        5
        >>> str(c)
        'lorem'
        >>> c.max_size = 15
        >>> str(c)
        'lorem ipsum dol'
    """

    def __new__(cls, txt, frmt=ConsoleString.align_left, *args, **kw):
        return ConsoleString.__new__(cls, txt, frmt)

    def __init__(self, txt, frmt=ConsoleString.align_left,
                 tag_beg="", tag_end="", color=False):
        super().__init__(txt, frmt)
        self.max_size = len(txt)
        self.tag_beg = tag_beg
        self.tag_end = tag_end

    def __len__(self):
        return self.max_size + len(self.tag_beg) + len(self.tag_end)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
