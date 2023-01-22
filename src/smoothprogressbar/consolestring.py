#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
"""Define ConsoleString."""

from __future__ import annotations

from typing import Optional


class ConsoleString:
    """Print messages.

    Console string is a string to print (stdout) with
    fixed size.

    '[XXXXXXXXX ]                  '
     -          -                    : tag size
      ----------                     : text size
    |------------------------------| : max size

    Why:
        It's usefull to manage the screen size.

    Use:
        >>> c = ConsoleString("lorem", max_size=3)
        >>> c
        lor
        >>> c = ConsoleString("lorem")
        >>> # tag
        >>> c.tag_beg = "["
        >>> c.tag_end="]"
        >>> for i in range(9): c.max_size = i ; str(c)
        ''
        '['
        '[]'
        '[l]'
        '[lo]'
        '[lor]'
        '[lore]'
        '[lorem]'
        '[lorem] '
        >>> len(c)
        8
        >>> c.text
        'lorem'
        >>> c = ConsoleString("lorem")
        >>> for i in range(9): c.max_size = i ; str(c.align_left())
        ''
        'l'
        'lo'
        'lor'
        'lore'
        'lorem'
        'lorem '
        'lorem  '
        'lorem   '
        >>> c = ConsoleString("lorem")
        >>> for i in range(9): c.max_size = i ; str(c.align_right())
        ''
        'l'
        'lo'
        'lor'
        'lore'
        'lorem'
        ' lorem'
        '  lorem'
        '   lorem'
        >>> txt = "lorem ipsum dolor sit amet consectetur adipiscing elit"
        >>> str(c.update(text=txt, max_size=15, tag_beg="*** "))
        '*** lorem ipsum'
    """

    def __init__(self, text: str, max_size: int = 0, tag_beg: str = "",
                 tag_end: str = "", enable: bool = True) -> None:
        """Init ConsoleString."""
        self.__enable: bool = enable
        self.__align: str = "<"
        self.__max_size: int = 0
        self.max_size: int = max_size
        self.text: str = text
        self.tag_beg: str = tag_beg
        self.tag_end: str = tag_end

    @property
    def enable(self) -> bool:
        """Get enable."""
        return self.__enable

    @property
    def max_size(self) -> int:
        """Get max size."""
        return self.__max_size

    @max_size.setter
    def max_size(self, value: int) -> None:
        """Set max size."""
        if isinstance(value, int):
            self.__max_size = value
        else:
            raise TypeError(
                f"invalid literal for int() with base 10: '{value}'")

    @property
    def tag_size(self) -> int:
        """Get tag_size."""
        return len(self.tag_beg + self.tag_end)

    @property
    def max_text_size(self) -> int:
        """Get max_text_size."""
        return max(0, int(self.max_size) - int(self.tag_size))

    @property
    def current_text_size(self) -> int:
        """Get current_text_size."""
        return min(self.max_text_size, len(self.text))

    def align_left(self) -> ConsoleString:
        """Apply 'align-left' to the string."""
        self.__align = "<"
        return self

    def align_right(self) -> ConsoleString:
        """Apply 'align-right' to the string."""
        self.__align = ">"
        return self

    def update(self, text: Optional[str] = None,
               max_size: Optional[int] = None,
               tag_beg: Optional[str] = None,
               tag_end: Optional[str] = None) -> ConsoleString:
        """Update the string."""
        if text is not None:
            self.text = text
        if max_size is not None:
            self.max_size = max_size
        if tag_beg is not None:
            self.tag_beg = tag_beg
        if tag_end is not None:
            self.tag_end = tag_end
        return self

    def __len__(self) -> int:
        """Get len()."""
        return len(str(self))

    def __repr__(self) -> str:
        """Get ConsoleString repr()."""
        txt = self.tag_beg + self.text[0:self.current_text_size] + self.tag_end
        result = f'{txt: {self.__align}{self.max_size}}'
        return result[0:self.max_size]

    def __str__(self) -> str:
        """Get ConsoleString str()."""
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
