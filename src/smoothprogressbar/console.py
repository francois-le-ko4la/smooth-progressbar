#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define Console."""

from __future__ import annotations

import shutil
import sys

from smoothprogressbar.__config__ import Theme


class Console:
    """
    This Class provides a simple way to manage the screen.

    Use:
        >>> c = Console()
        >>> c.addmsg("lorem ipsum dolor").print()
        lorem ipsum dolor
        >>> c.addmsg("lorem ipsum dolor").newline().addmsg("LOREM").print()
        lorem ipsum dolor
        LOREM
    """

    def __init__(self) -> None:
        """Init."""
        self.__output = ""

    @property
    def size(self) -> int:
        """Get screen size."""
        return int(shutil.get_terminal_size().columns)

    def addmsg(self, msg: str) -> Console:
        """Store a message."""
        self.__output = f"{self.__output}{msg}"
        return self

    def emptyline(self) -> Console:
        """Add an empty line."""
        self.__output = f"{self.__output}{' ' * self.size}"
        return self

    def addtab(self) -> Console:
        """Add tab."""
        self.__output = f"{self.__output}{Theme.TAB.value}"
        return self

    def goback(self) -> Console:
        """Go back."""
        self.__output = f"{self.__output}{Theme.GOBACK.value}"
        return self

    def newline(self) -> Console:
        """Add a new line."""
        self.__output = f"{self.__output}{Theme.LINEFEED.value}"
        return self

    def print(self) -> None:
        """Print the buffer."""
        sys.stdout.write(self.__output)
        sys.stdout.flush()
        self.__output = ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
