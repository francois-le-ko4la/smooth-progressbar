#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####   ######  #####    ####   ######  #    #   #####
 #    #  #       #    #  #    #  #       ##   #     #
 #    #  #####   #    #  #       #####   # #  #     #
 #####   #       #####   #       #       #  # #     #
 #       #       #   #   #    #  #       #   ##     #
 #       ######  #    #   ####   ######  #    #     #

"""


class Percent(float):
    """
    Calc

    Use:
        >>> #oups 1
        >>> p = Percent(0)
        Traceback (most recent call last):
        ...
        ValueError: Percent: "whole" cant be 0
        >>> #oups 3
        >>> p = Percent(10)
        >>> p.value = 10
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        >>> #correct usage:
        >>> p = Percent(10)
        >>> p.part = 2
        >>> p.part
        2
        >>> p
        20.0%
        >>> str(p)
        '20.0%'
        >>> p.value
        0.2
        >>> p = Percent(8)
        >>> for i in range(9): p.part = i ; print("{}-{}".format(p, p.value))
        0.0%-0.0
        12.5%-0.125
        25.0%-0.25
        37.5%-0.375
        50.0%-0.5
        62.5%-0.625
        75.0%-0.75
        87.5%-0.875
        100.0%-1.0
    """

    def __new__(cls, whole):
        return super(Percent, cls).__new__(cls, whole)

    def __init__(self, whole):
        super().__init__()
        if whole is 0:
            raise ValueError("Percent: \"whole\" cant be 0")
        self.__part = 0

    @property
    def whole(self):
        """
            X% = 100 * (part / whole)
        """
        return float(super().__repr__())

    @property
    def part(self):
        """
            X% = 100 * (part / whole)
        """
        return self.__part

    @part.setter
    def part(self, part):
        self.__part = part

    @property
    def value(self):
        """
            value = X%/100 = part / whole
        """
        return float(self.part) / self.whole

    def __repr__(self):
        """
            str: "XXX.X%"
        """
        return "{:.1%}".format(self.value)

    def __str__(self):
        return str(self.__repr__())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
