#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from smoothprogressbar.consolestring import ConsoleString
from smoothprogressbar import __config__

class ConsolePercent(ConsoleString):
    """

    Why:
        It's usefull to manage the screen size.

    Use:
        >>> str(ConsolePercent("1.0%"))
        '[  1.0%]'
        >>> len(ConsolePercent("1.0%"))
        8
        >>> str(ConsolePercent("40.0%"))
        '[ 40.0%]'
        >>> len(ConsolePercent("40.0%"))
        8
        >>> str(ConsolePercent("100.%"))
        '[ 100.%]'
        >>> len(ConsolePercent("100.%"))
        8
    """

    def __new__(cls, percent, frmt=ConsoleString.align_right, *args, **kw):
        return ConsoleString.__new__(cls, percent, frmt)

    def __init__(self, percent, frmt=ConsoleString.align_right, tag_beg=__config__.ProgressTheme.beggining, tag_end=__config__.ProgressTheme.end):
        super().__init__(percent, frmt)
        self.max_size = 6
        self.tag_beg = tag_beg
        self.tag_end = tag_end

    def __len__(self):
        return self.max_size + len(self.tag_beg) + len(self.tag_end)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
