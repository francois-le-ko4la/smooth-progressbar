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
from smoothprogressbar.__config__ import THEME


class ConsoleProgress(ConsoleString):

    """
    Use:
        >>> c = ConsoleProgress()
        >>> str(c.update(12, 0.1))
        '[#.........]'
        >>> str(c.update(12, 0.4))
        '[####......]'
        >>> str(c.update(12, 1))
        '[##########]'
        >>> len(c.update(12, 1))
        12
    """

    def __init__(self, tag_beg=THEME["beggining"], tag_end=THEME["end"]):
        super().__init__("")
        self.tag_beg = tag_beg
        self.tag_end = tag_end

    def update(self, size, ratio):
        if ratio >= 0 and ratio <= 1:
            self.max_size = size
            self.text = '{0:{fill}{align}{size}}'.format(
                THEME["done"] * int(self.max_text_size * ratio),
                fill=THEME["not_done"],
                align="<",
                size=self.max_text_size
            )
            return self
        else:
            raise ValueError("Wrong ratio")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
