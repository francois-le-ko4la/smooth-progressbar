#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes, consider-using-with
"""Define Prgbr."""

from __future__ import annotations

from threading import Lock

from smoothprogressbar.__config__ import Theme
from smoothprogressbar.console import Console
from smoothprogressbar.consoleprgbr import ConsolePrgBr
from smoothprogressbar.elapse import ElapseTime
from smoothprogressbar.multithreading import MultiThread
from smoothprogressbar.percent import Percent


class SmoothProgressBar:
    """This class use all others component to manage the progressbar."""

    __size: int
    __percent: Percent
    __msg: str

    def __init__(self, enable_elapse: bool = True, enable_msg: bool = True,
                 debug: bool = False) -> None:
        """Init."""
        self.__debug: bool = debug
        self.__prgbr: ConsolePrgBr = ConsolePrgBr(
            enable_elapse, enable_msg, debug=debug)
        self.__enable_msg: bool = enable_msg
        self.__console: Console = Console()
        self.__elapse: ElapseTime = ElapseTime()
        self.__mthr: MultiThread = MultiThread(
            self.__refresh, Theme.REFRESH_TIME.value)
        self.__updated: bool = False
        self.__lock = Lock()

    @property
    def msg(self) -> str:
        """Get message."""
        return self.__msg

    @msg.setter
    def msg(self, msg: str) -> None:
        """Set message."""
        self.__msg = msg
        self.__updated = True
        self.__refresh()

    def start(self, max_value: int) -> None:
        """Start the progress bar.

        init percent(), screen size, elapse & multithreading
        """
        self.__percent = Percent(max_value)
        self.__size = int(self.__console.size) - 1
        self.__elapse.start()
        self.__mthr.start()

    def stop(self) -> None:
        """Stop the progress bar."""
        self.__console.goback()
        self.__console.emptyline()
        self.__console.goback()
        self.__console.print()
        self.__mthr.stop()

    def update(self, value: int, msg: str = "") -> None:
        """Update the progressbar."""
        self.__updated = True
        self.__percent.part = value
        self.__msg = msg
        # self.__refresh()

    def __refresh(self) -> None:
        if self.__updated is not True:
            return

        self.__lock.acquire()
        self.__size = int(self.__console.size) - 1
        if self.__debug is not True:
            self.__console.goback()
        if self.__enable_msg is not True:
            self.__console.emptyline().goback().addmsg(self.__msg).newline()

        self.__console.addmsg(
            self.__prgbr.update(
                self.__size,
                self.__percent,
                self.__msg,
                str(self.__elapse)
            ).get()
        )
        self.__console.goback()
        self.__console.print()
        self.__updated = False
        self.__lock.release()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
