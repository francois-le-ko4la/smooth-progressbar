#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define ConsolePrgBr."""

from __future__ import annotations

from smoothprogressbar.__config__ import Theme
from smoothprogressbar.consoleprogress import ConsoleProgress
from smoothprogressbar.consolestring import ConsoleString
from smoothprogressbar.percent import Percent


class ConsolePrgBr:
    """
    This class print all components according to parameters.

    Use:
    >>> from smoothprogressbar.percent import Percent
    >>> from smoothprogressbar.elapse import ElapseTime
    >>> size = 40
    >>> percent = Percent(10)
    >>> percent.part = 2
    >>> msg = "lorem ipsum dolor sit amet consectetur adipiscing elit"
    >>> elapse = ElapseTime()
    >>> elapse.start()
    >>> prgbr = ConsolePrgBr(debug=True)
    >>> prgbr.update(size, percent, msg, str(elapse)).get()
    'Processing: [ 20.0%] [...] 0:00:00 lorem'
    >>> size = 70
    >>> prgbr = ConsolePrgBr(debug=True)
    >>> prgbr.update(size, percent, msg, str(elapse)).get()
    'Processing: [ 20.0%] [###...............] 0:00:00 lorem ipsum dolor si'
    >>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=False, debug=True)
    >>> prgbr.update(size, percent, msg, str(elapse)).get()
    'Processing: [ 20.0%] [#########......................................]'
    >>> prgbr = ConsolePrgBr(enable_elapse=True, enable_msg=False, debug=True)
    >>> prgbr.update(size, percent, msg, str(elapse)).get()
    'Processing: [ 20.0%] [#######................................] 0:00:00'
    >>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=True, debug=True)
    >>> prgbr.update(size, percent, msg, str(elapse)).get()
    'Processing: [ 20.0%] [####..................] lorem ipsum dolor sit am'

    """

    progress_label = "Processing: "
    size_widgt_label_label = len(progress_label)
    size_widgt_percent = 5

    def __init__(self, enable_elapse: bool = True, enable_msg: bool = True,
                 debug: bool = False) -> None:
        """Init."""
        self.__debug = debug
        self.__output = ""
        """ DEF """
        self.__widgt_label = ConsoleString(Theme.LABEL.value,
                                           len(Theme.LABEL.value))
        self.__widgt_percent = ConsoleString(
            "",
            max_size=8,
            tag_beg=Theme.BEG.value,
            tag_end=Theme.END.value
        )
        self.__widgt_elapse = ConsoleString("", enable=enable_elapse)
        self.__widgt_msg = ConsoleString("", tag_beg=" ", enable=enable_msg)
        self.__widgt_progress = ConsoleProgress(
            tag_beg=" " + Theme.BEG.value)

    def update(self, size: int, percent: Percent,
               msg: str = "", elapse: str = "") -> ConsolePrgBr:
        """Update the progress bar."""
        if self.__widgt_elapse.enable:
            self.__widgt_elapse.max_size = 8
        else:
            self.__widgt_elapse.max_size = 0

        psize = size - self.__widgt_label.max_size - \
            len(self.__widgt_percent) - self.__widgt_elapse.max_size

        self.__widgt_msg.update(msg)
        if self.__widgt_msg.enable:
            size_widgt_progress = int(0.5 * psize)
            self.__widgt_msg.max_size = psize - size_widgt_progress
        else:
            size_widgt_progress = psize
            self.__widgt_msg.max_size = 0

        color_start: str = Theme.INFO.value
        color_stop: str = Theme.RESET.value
        if self.__debug:
            color_start = ""
            color_stop = ""

        self.__output = "".join([
            color_start,
            str(self.__widgt_label),
            str(self.__widgt_percent.update(str(percent))),
            color_stop,
            str(self.__widgt_progress.update(
                size_widgt_progress, percent.value)),
            str(self.__widgt_elapse.update(elapse).align_right()),
            str(self.__widgt_msg.update(msg))])
        return self

    def get(self) -> str:
        """Get the string."""
        return str(self)

    def __repr__(self) -> str:
        """Get repr()."""
        return self.__output

    def __str__(self) -> str:
        """Get str()."""
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
