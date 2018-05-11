#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####
#     #  #    #   ####    ####    #####  #    #
#        ##  ##  #    #  #    #     #    #    #
 #####   # ## #  #    #  #    #     #    ######
      #  #    #  #    #  #    #     #    #    #
#     #  #    #  #    #  #    #     #    #    #
 #####   #    #   ####    ####      #    #    # Progress Bar

"""

from threading import Lock
from smoothprogressbar.elapse import ElapseTime
from smoothprogressbar.percent import Percent
from smoothprogressbar.consoleprgbr import ConsolePrgBr
from smoothprogressbar.console import Console
from smoothprogressbar.multithreading import MultiThread
from smoothprogressbar import __config__


class SmoothProgressBar(object):
    """
    This class use all others component to manage the progressbar.

    Use:

    """
    def __init__(self, enable_elapse=True, enable_msg=True, debug=False):
        self.__debug = debug
        self.__prgbr = ConsolePrgBr(enable_elapse, enable_msg, debug=debug)
        self.__enable_msg = enable_msg
        self.__percent = None
        self.__console = Console()
        self.__size = None
        self.__elapse = ElapseTime()
        self.__mthr = MultiThread(self.__refresh, 0.25)
        self.__updated = False
        self.__lock = Lock()

    @property
    def msg(self):
        """
        Message
        """
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg
        self.__updated = True
        self.__refresh()

    def start(self, max_value):
        """
        start the progress bar
            init percent(), screen size, elapse & multithreading
        """
        self.__percent = Percent(max_value)
        self.__size = int(self.__console.size) - 1
        self.__elapse.start()
        self.__mthr.start()

    def stop(self):
        """
        stop the progress bar
        """
        self.__console.goback()
        self.__console.addmsg(" " * self.__size)
        self.__console.goback()
        self.__console.print()
        self.__mthr.stop()

    def update(self, value, msg=""):
        """
        update the progressbar
        """
        self.__updated = True
        self.__percent.part = value
        self.__msg = msg

    def __refresh(self):
        if self.__updated is not True:
            return

        self.__lock.acquire()
        prgbr = self.__prgbr.build_progressbar(self.__size,
                                               self.__percent,
                                               self.__msg,
                                               str(self.__elapse)
                                               )
        if self.__debug is not True:
            self.__console.goback()
        if self.__enable_msg is not True:
            self.__console.addmsg(" " * self.__size)
            self.__console.goback()
            self.__console.addmsg(self.__msg)
            self.__console.newline()

        self.__console.addmsg(prgbr)
        self.__console.print()
        self.__updated = False
        self.__lock.release()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
