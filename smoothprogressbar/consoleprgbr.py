#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####   #####   #####    ####   #####   #####
 #    #  #    #  #    #  #    #  #    #  #    #
 #       #    #  #    #  #       #####   #    #
 #       #####   #####   #  ###  #    #  #####
 #    #  #       #   #   #    #  #    #  #   #
  ####   #       #    #   ####   #####   #    #

"""

from smoothprogressbar.consolestring import ConsoleString
from smoothprogressbar.consoleprogress import ConsoleProgress
from smoothprogressbar.__config__ import THEME


class ConsolePrgBr(object):

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

    def __init__(self, enable_elapse=True, enable_msg=True, debug=False):
        self.__debug = debug
        self.__output = ""
        """ DEF """
        self.__widgt_label = ConsoleString(THEME["label"], len(THEME["label"]))
        self.__widgt_percent = ConsoleString(
            "",
            max_size=8,
            tag_beg=THEME["beggining"],
            tag_end=THEME["end"]
        )
        self.__widgt_elapse = ConsoleString("", enable=enable_elapse)
        self.__widgt_msg = ConsoleString("", tag_beg=" ", enable=enable_msg)
        self.__widgt_progress = ConsoleProgress(
            tag_beg=" " + THEME["beggining"])

    def update(self, size, percent, msg="", elapse=""):
        """
        Update() the progress bar
        """
        size_widgt_progress = 0
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

        color_start = THEME["info"]
        color_stop = THEME["reset"]
        if self.__debug:
            color_start = ""
            color_stop = ""

        self.__output = "{}{}{}{}{}{}{}".format(
            color_start,
            self.__widgt_label,
            self.__widgt_percent.update(str(percent)),
            color_stop,
            self.__widgt_progress.update(size_widgt_progress, percent.value),
            self.__widgt_elapse.update(elapse).align_right(),
            self.__widgt_msg.update(msg)
        )
        return self

    def get(self):
        """
        Get the string
        """
        return str(self)

    def __repr__(self):
        return self.__output

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
