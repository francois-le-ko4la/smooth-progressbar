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

import subprocess
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
    def size(self):
        """
        screen size (columns)
        """
        p = subprocess.Popen('stty size', stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        self.__rows, self.__columns = output.split()
        return self.__columns.decode('UTF-8')

    def addmsg(self, msg):
        """
        store a message
        """
        self.__output += msg

    def emptyline(self):
        """
        store an empty line
        """
        self.__output += " "

    def addtab(self):
        """
        store a tab
        """
        self.__output += "\t"

    def goback(self):
        """
        store a goback caracter
        """
        self.__output += "\r"

    def newline(self):
        """
        store a new line
        """
        self.__output += "\n"

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
