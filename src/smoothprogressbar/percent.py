#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module calc percentage."""

from __future__ import annotations


class Percent(float):
    """Calc percent.

    Use:
        >>> p = Percent(10)
        >>> p.part = 2
        >>> p.part
        2
        >>> p
         20.0%
        >>> str(p)
        ' 20.0%'
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

    def __new__(cls, whole: float) -> "Percent":
        """Do new."""
        return super(Percent, cls).__new__(cls, whole)

    def __init__(self, whole: int) -> None:
        """Init."""
        super().__init__()
        if whole == 0:
            raise ValueError('Percent: "whole" cant be 0')
        self.__part = 0

    @property
    def whole(self) -> float:
        """Get whole.

        Returns:
            float: X% = 100 * (part / whole)
        """
        return float(super().__repr__())

    @property
    def part(self) -> int:
        """Get part.

        Returns:
            int: X% = 100 * (part / whole)
        """
        return self.__part

    @part.setter
    def part(self, value: int) -> None:
        """Set part."""
        if isinstance(value, int):
            self.__part = value
        else:
            raise TypeError(
                f"invalid literal for int() with base 10: '{value}'")

    @property
    def value(self) -> float:
        """Get Value.

        Returns:
            float: value = X%/100 = part / whole
        """
        return float(self.part) / self.whole

    def __repr__(self) -> str:
        """Get str.

        Returns:
            str: "XXX.X%"
        """
        return f'{self.value : >6.1%}'

    def __str__(self) -> str:
        """Get str.

        Returns:
            str: "XXX.X%"
        """
        return str(self.__repr__())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
