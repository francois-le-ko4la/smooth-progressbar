#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

from smoothprogressbar.consolestring import ConsoleString
from smoothprogressbar.consolelabel import ConsoleLabel
from smoothprogressbar.consoleprogress import ConsoleProgress
from smoothprogressbar.percent import Percent
from smoothprogressbar.consolepercent import ConsolePercent
from smoothprogressbar import __config__


class ConsolePrgBr(object):

    """
    Use:
    >>> from smoothprogressbar.elapse import ElapseTime
    >>> size = 40
    >>> percent = Percent(10)
    >>> percent.value = 2
    >>> msg = "lorem ipsum dolor sit amet consectetur adipiscing elit"
    >>> elapse = ElapseTime()
    >>> elapse.start()
    >>> prgbr = ConsolePrgBr(debug=True)
    >>> prgbr.build_progressbar(size, percent, msg, str(elapse))
    'Processing: [ 20.0%] [...] 0:00:00 lorem'
    >>> size = 70
    >>> prgbr = ConsolePrgBr(debug=True)
    >>> prgbr.build_progressbar(size, percent, msg, str(elapse))
    'Processing: [ 20.0%] [###...............] 0:00:00 lorem ipsum dolor si'
    >>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=False, debug=True)
    >>> prgbr.build_progressbar(size, percent, msg, str(elapse))
    'Processing: [ 20.0%] [#########......................................]'
    >>> prgbr = ConsolePrgBr(enable_elapse=True, enable_msg=False, debug=True)
    >>> prgbr.build_progressbar(size, percent, msg, str(elapse))
    'Processing: [ 20.0%] [#######................................] 0:00:00'
    >>> prgbr = ConsolePrgBr(enable_elapse=False, enable_msg=True, debug=True)
    >>> prgbr.build_progressbar(size, percent, msg, str(elapse))
    'Processing: [ 20.0%] [####..................] lorem ipsum dolor sit am'

    """
    progress_label = "Processing: "
    size_widgt_label_label = len(progress_label)
    size_widgt_percent = 5

    def __init__(self, enable_elapse=True, enable_msg=True, debug=False):
        self.__debug = debug
        self.__enable_elapse = enable_elapse
        self.__enable_msg = enable_msg
        """ DEF """
        self.__widgt_label = ConsoleLabel("")
        self.__widgt_percent = ConsolePercent(Percent(1))
        self.__widgt_progress = ConsoleProgress(1, 1)

    def build_progressbar(self, size, percent, msg="", elapse=""):
        """
        fixed size
        """
        widgt_label = ConsoleLabel(__config__.ProgressTheme.label)
        widgt_percent = ConsolePercent(percent)
        widgt_elapse = ConsoleLabel(elapse, ConsoleString.align_right)
        if self.__enable_elapse:
            widgt_elapse.max_size = 8
        else:
            widgt_elapse.max_size = 0

        """
        other
        """
        psize = size - widgt_label.max_size - len(widgt_percent) - \
            widgt_elapse.max_size

        widgt_msg = ConsoleLabel(" " + msg)
        if self.__enable_msg:
            size_widgt_progress = int(0.5 * psize) - 1
            widgt_msg.max_size = psize - size_widgt_progress - 1
        else:
            size_widgt_progress = psize - 1
            widgt_msg.max_size = 0

        widgt_bar = ConsoleProgress(size_widgt_progress, percent.ratio)

        color_start = __config__.Color.info
        color_stop = __config__.Color.reset
        if self.__debug:
            color_start = ""
            color_stop = ""

        return "{}{}{}{} {}{}{}".format(color_start,
                                        widgt_label,
                                        widgt_percent,
                                        color_stop,
                                        widgt_bar,
                                        widgt_elapse,
                                        widgt_msg
                                        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
