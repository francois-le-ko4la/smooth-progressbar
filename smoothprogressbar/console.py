#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

  ####    ####   #    #   ####    ####   #       ######
 #    #  #    #  ##   #  #       #    #  #       #
 #       #    #  # #  #   ####   #    #  #       #####
 #       #    #  #  # #       #  #    #  #       #
 #    #  #    #  #   ##  #    #  #    #  #       #
  ####    ####   #    #   ####    ####   ######  ######

"""

import shutil
import subprocess
import sys
from smoothprogressbar.__config__ import THEME


class Console(object):

    """
    This Class provides a simple way to manage the screen

    Use:
        >>> c = Console()
        >>> c.addmsg("lorem ipsum dolor").print()
        lorem ipsum dolor
        >>> c.addmsg("lorem ipsum dolor").newline().addmsg("LOREM").print()
        lorem ipsum dolor
        LOREM
    """

    def __init__(self):
        self.__rows = None
        self.__columns = None
        self.__output = ""

    @property
    def size(self):
        """
        screen size (columns)
        """
        return int(shutil.get_terminal_size().columns)

    def addmsg(self, msg):
        """
        store a message
        """
        self.__output += msg
        return self

    def emptyline(self):
        """
        store an empty line
        """
        self.__output += " " * self.size
        return self

    def addtab(self):
        """
        store a tab
        """
        self.__output += THEME["tab"]
        return self

    def goback(self):
        """
        store a goback caracter
        """
        self.__output += THEME["goback"]
        return self

    def newline(self):
        """
        store a new line
        """
        self.__output += THEME["linefeed"]
        return self

    def print(self):
        """
        print the buffer
        """
        sys.stdout.write(self.__output)
        sys.stdout.flush()
        self.__output = ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
