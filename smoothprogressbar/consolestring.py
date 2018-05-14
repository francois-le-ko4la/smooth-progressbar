#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

  ####    #####  #####      #    #    #   ####
 #          #    #    #     #    ##   #  #    #
  ####      #    #    #     #    # #  #  #
      #     #    #####      #    #  # #  #  ###
 #    #     #    #   #      #    #   ##  #    #
  ####      #    #    #     #    #    #   ####

"""


class ConsoleString(object):
    """
    Console string is a string to print (stdout) with
    fixed size.

    '[XXXXXXXXX ]                  '
     -          -                    : tag size
      ----------                     : text size
    |------------------------------| : max size

    Why:
        It's usefull to manage the screen size.

    Use:
        >>> #oups
        >>> c = ConsoleString("lorem", max_size="3")
        Traceback (most recent call last):
        ...
        TypeError: invalid literal for int() with base 10: '3'
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

    def __init__(self, text, max_size=0, tag_beg="", tag_end="", enable=True):
        self.__enable = enable
        self.__align = "<"
        self.__max_size = 0
        self.max_size = max_size
        self.text = text
        self.tag_beg = tag_beg
        self.tag_end = tag_end

    @property
    def enable(self):
        """
        Enable object
        """
        return self.__enable

    @property
    def max_size(self):
        """
        string max size
        """
        return self.__max_size

    @max_size.setter
    def max_size(self, value):
        if isinstance(value, int):
            self.__max_size = value
        else:
            raise TypeError(
                "invalid literal for int() with base 10: '{}'".format(
                    value
                )
            )

    @property
    def tag_size(self):
        """
        Tag size
        """
        return len(self.tag_beg + self.tag_end)

    @property
    def max_text_size(self):
        """
        Tag size setter
        """
        return max(0, int(self.max_size) - int(self.tag_size))

    @property
    def current_text_size(self):
        """
        Text size according to text_size and max_text_size
            min(text_size, len(text))
        """
        return min(self.max_text_size, len(self.text))

    def align_left(self):
        """
        Apply 'align-left' to the string
        """
        self.__align = "<"
        return self

    def align_right(self):
        """
        Apply 'align-right' to the string
        """
        self.__align = ">"
        return self

    def update(self, text=None, max_size=None, tag_beg=None, tag_end=None):
        """
        update the string
        """
        if text is not None:
            self.text = text
        if max_size is not None:
            self.max_size = max_size
        if tag_beg is not None:
            self.tag_beg = tag_beg
        if tag_end is not None:
            self.tag_end = tag_end
        return self

    def __len__(self):
        return len(str(self))

    def __repr__(self):
        result = '{0:{fill}{align}{size}}'.format(
            self.tag_beg + self.text[0:self.current_text_size] + self.tag_end,
            fill=" ",
            align=self.__align,
            size=self.max_size
        )
        return result[0:self.max_size]

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
