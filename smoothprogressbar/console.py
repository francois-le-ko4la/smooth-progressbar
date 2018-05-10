#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import os
import sys


class Console(object):

    """
    This Class provides a simple way to manage the screen

    Use:
        >>> c = Console()
        >>> c.addmsg("lorem ipsum dolor sit amet consectetur adipiscing elit")
        >>> c.print()
        lorem ipsum dolor sit amet consectetur adipiscing elit
        >>> c.addmsg("lorem ipsum dolor sit amet consectetur adipiscing elit")
        >>> c.newline()
        >>> c.addmsg("LOREM")
        >>> c.print()
        lorem ipsum dolor sit amet consectetur adipiscing elit
        LOREM
    """

    def __init__(self):
        self.__rows = None
        self.__columns = None
        self.__output = ""

    @property
    def row(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.__rows = rows
        return self.__rows

    @property
    def colums(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.__columns = columns
        return self.__columns

    def addmsg(self, msg):
        self.__output += msg

    def emptyline(self):
        self.__output += " "

    def addtab(self):
        self.__output += "\t"

    def goback(self):
        self.__output += "\r"

    def newline(self):
        self.__output += "\n"

    def print(self):
        sys.stdout.write(self.__output)
        sys.stdout.flush()
        self.__output = ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
