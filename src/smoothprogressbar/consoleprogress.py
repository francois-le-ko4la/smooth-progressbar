#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=arguments-differ
# mypy: disable-error-code=override
"""Define ConsoleProgress."""

from __future__ import annotations

from smoothprogressbar.__config__ import Theme
from smoothprogressbar.consolestring import ConsoleString


class ConsoleProgress(ConsoleString):
    """Define ConsoleProgress.

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

    def __init__(self, tag_beg: str = Theme.BEG.value,
                 tag_end: str = Theme.END.value) -> None:
        """Init."""
        super().__init__("")
        self.tag_beg = tag_beg
        self.tag_end = tag_end

    def update(self, size: int, ratio: float) -> ConsoleProgress:
        """Update."""
        if 0 <= ratio <= 1:
            self.max_size = size
            txt = Theme.DONE.value * int(self.max_text_size * ratio)
            self.text = f'{txt:{Theme.NOT_DONE.value}<{self.max_text_size}}'
            return self
        raise ValueError("Wrong ratio")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
