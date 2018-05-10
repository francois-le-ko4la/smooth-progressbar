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

import time
from threading import Lock
from smoothprogressbar.elapse import ElapseTime
from smoothprogressbar.percent import Percent
from smoothprogressbar.consoleprgbr import ConsolePrgBr
from smoothprogressbar.console import Console
from smoothprogressbar.multithreading import MultiThread
from smoothprogressbar import __config__


class SmoothProgressBar(object):
    def __init__(self, enable_elapse=True, enable_msg=True):
        self.__prgbr = ConsolePrgBr(enable_elapse, enable_msg)
        self.__enable_msg = enable_msg
        self.__percent = None
        self.__console = Console()
        self.__elapse = ElapseTime()
        self.__mthr = MultiThread(self.__refresh, 0.25)
        self.__updated = False
        self.__lock = Lock()

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg
        self.__updated = True
        self.__refresh()

    def start(self, max_value):
        self.__percent = Percent(max_value)
        self.__elapse.start()
        self.__mthr.start()

    def stop(self):
        self.__console.goback()
        self.__console.addmsg(" " * int(self.__console.colums))
        self.__console.goback()
        self.__console.print()
        self.__mthr.stop()

    def update(self, value, msg=""):
        self.__updated = True
        self.__percent.value = value
        self.__msg = msg

    def __refresh(self):
        if self.__updated is not True:
            return

        self.__lock.acquire()
        prgbr = self.__prgbr.build_progressbar(int(self.__console.colums) - 1,
                                               self.__percent,
                                               self.__msg,
                                               str(self.__elapse)
                                               )
        self.__console.goback()
        if self.__enable_msg is not True:
            self.__console.addmsg(" " * int(self.__console.colums))
            self.__console.goback()
            self.__console.addmsg(self.__msg)
            self.__console.newline()
        self.__console.addmsg(prgbr)
        self.__console.print()
        self.__updated = False
        self.__lock.release()
