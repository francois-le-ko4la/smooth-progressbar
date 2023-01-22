#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module calc elapse time."""
from __future__ import annotations

import datetime
from typing import Optional


class ElapseTime:
    """
    Calculate elapse time.

    Use:
        >>> import time
        >>> t = ElapseTime()
        >>> #oups...
        >>> t
        Traceback (most recent call last):
        ...
        RuntimeError: start before...
        >>> t.start()
        >>> time.sleep(1)
        >>> t
        0:00:01
        >>> time.sleep(1)
        >>> t
        0:00:02
        >>> str(t)
        '0:00:02'
    """

    def __init__(self) -> None:
        """Init the default values.

        Returns:
            obj

        """
        self.__start_time: Optional[datetime.datetime] = None
        self.__update_time: Optional[datetime.datetime] = None

    def start(self) -> None:
        """Store the current timestamp in self.__start_time.

        Returns:
            None

        """
        self.__start_time = datetime.datetime.now().replace(microsecond=0)

    def __repr__(self) -> str:
        """Provide the string.

        Returns:
            str: 'X:XX:XX'

        """
        if self.__start_time is None:
            raise RuntimeError("start before...")
        self.__update_time = datetime.datetime.now().replace(microsecond=0)

        return str((self.__update_time - self.__start_time))

    def __str__(self) -> str:
        """Call repr().

        Returns:
            str: 'X:XX:XX'

        """
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
