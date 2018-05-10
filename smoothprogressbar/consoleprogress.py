#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####
#     #  #    #   ####    ####    #####  #    #
#        ##  ##  #    #  #    #     #    #    #
 #####   # ## #  #    #  #    #     #    ######
      #  #    #  #    #  #    #     #    #    #
#     #  #    #  #    #  #    #     #    #    #
 #####   #    #   ####    ####      #    #    # Progress Bar

"""

from smoothprogressbar.consolestring import ConsoleString
from smoothprogressbar import __config__


class ConsoleProgress(ConsoleString):

    """
    Use:
        >>> str(ConsoleProgress(12, 0.1))
        '[#.........]'
        >>> str(ConsoleProgress(12, 0.4))
        '[####......]'
        >>> str(ConsoleProgress(12, 1))
        '[##########]'
        >>> len(ConsoleProgress(12, 1))
        12
    """

    def __new__(cls, size, ratio, frmt=ConsoleString.align_left,
                tag_beg=__config__.ProgressTheme.beggining,
                tag_end=__config__.ProgressTheme.end,
                block=__config__.ProgressTheme.done,
                empty=__config__.ProgressTheme.not_done, *args, **kw):
        size = size - len(tag_beg) - len(tag_end)
        block_size = int(ratio * size)
        empty_size = size - block_size
        txt = "{}{}".format(block * block_size, empty * empty_size)
        return ConsoleString.__new__(cls, txt, frmt)

    def __init__(self, size, ratio, frmt=ConsoleString.align_left,
                 tag_beg=__config__.ProgressTheme.beggining,
                 tag_end=__config__.ProgressTheme.end,
                 block=__config__.ProgressTheme.done,
                 empty=__config__.ProgressTheme.not_done):
        super().__init__("", frmt)
        if ratio >= 0 and ratio <= 1:
            self.max_size = size - len(tag_beg) - len(tag_end)
            self.tag_beg = tag_beg
            self.tag_end = tag_end
        else:
            raise ValueError("Wrong ratio")

    def __len__(self):
        return self.max_size + len(self.tag_beg) + len(self.tag_end)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
