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
from smoothprogressbar.elapse import ElapseTime
from smoothprogressbar.percent import Percent
from smoothprogressbar.consoleprgbr import ConsolePrgBr
from smoothprogressbar.console import Console
from smoothprogressbar import __config__


class SmoothProgressBar(object):
    def __init__(self, enable_elapse=True, enable_msg=True):
        self.__prgbr = ConsolePrgBr(enable_elapse, enable_msg)
        self.__enable_msg = enable_msg
        self.__percent = None
        self.__console = Console()
        self.__elapse = ElapseTime()

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg

    def start(self, max_value):
        self.__percent = Percent(max_value)
        self.__elapse.start()

    def stop(self):
        self.__console.goback()
        self.__console.addmsg(" " * int(self.__console.colums))
        self.__console.goback()
        self.__console.print()
        return

    def update(self, value, msg=""):
        self.__percent.value = value
        self.__msg = msg
        self.__refresh()


    def __refresh(self):
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

"""
prgbr = SmoothProgressBar(enable_msg=False)
prgbr.start(10)
prgbr.update(1,"txt1")
time.sleep(2)
prgbr.update(2,"txt2")
time.sleep(2)
prgbr.update(3,"txt3")

"""
