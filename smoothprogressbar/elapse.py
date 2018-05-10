#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######  #         ##    #####    ####   ######
 #       #        #  #   #    #  #       #
 #####   #       #    #  #    #   ####   #####
 #       #       ######  #####        #  #
 #       #       #    #  #       #    #  #
 ######  ######  #    #  #        ####   ######

"""

import datetime


class ElapseTime(object):
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

    def __init__(self):
        """
        Init the default values

        Args:
            None

        Returns:
            obj

        """
        self.__start_time = None
        self.__update_time = None

    def start(self):
        """
        Store the current timestamp in self.__start_time

        Args:
            None

        Returns:
            None

        """
        self.__start_time = datetime.datetime.now().replace(microsecond=0)

    def __repr__(self):
        """
        Provides the string

        Args:
            None

        Returns:
            None

        """
        if self.__start_time is None:
            raise RuntimeError("start before...")
        self.__update_time = datetime.datetime.now().replace(microsecond=0)

        return str((self.__update_time - self.__start_time))

    def __str__(self):
        """
        Call repr

        Args:
            None

        Returns:
            None

        """
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
