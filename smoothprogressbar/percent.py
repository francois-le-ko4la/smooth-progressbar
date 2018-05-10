#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from smoothprogressbar.consolestring import ConsoleString


class Percent(float):
    """
    Calc

    Use:
        >>> #oups 1
        >>> p = Percent(0)
        Traceback (most recent call last):
        ...
        ValueError: max_value cant be 0
        >>> #oups 3
        >>> p = Percent(10)
        >>> p.ratio = 10
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        >>> #correct usage:
        >>> p = Percent(10)
        >>> p.value = 2
        >>> p.value
        2
        >>> p
        20.0%
        >>> str(p)
        '20.0%'
        >>> p.ratio
        0.2
        >>> p = Percent(8)
        >>> for i in range(9): p.value = i ; print("{}-{}".format(p, p.ratio))
        0.0%-0.0
        12.5%-0.125
        25.0%-0.25
        37.5%-0.375
        50.0%-0.5
        62.5%-0.625
        75.0%-0.75
        87.5%-0.875
        100.%-1.0
    """

    def __init__(self, max_value):
        if max_value is 0:
            raise ValueError("max_value cant be 0")
        self.__value = 0

    @property
    def max_value(self):
        return float(super().__repr__())

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def ratio(self):
        return float(self.__value) / self.max_value

    def __repr__(self):
        """
        percent = str((self.get_percent() * 100))[0:4]
        return " " * (5 - len(percent)) + percent
        """
        return "{}%".format(str(round(100 * self.ratio, 1))[0:4])

    def __str__(self):
        return str(self.__repr__())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
