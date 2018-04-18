#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
                           _   _
 ___ _ __ ___   ___   ___ | |_| |__
/ __| '_ ` _ \ / _ \ / _ \| __| '_ \
\__ \ | | | | | (_) | (_) | |_| | | |
|___/_| |_| |_|\___/ \___/ \__|_| |_| Progress Bar


"""
import os
import sys
from threading import Timer
import datetime
from functools import wraps


class ProgressTheme:
    done = '#'
    not_done = '.'
    beggining = '['
    end = ']'
    first_description = "Starting..."

class Colors:
    reset = '\x1b[0m'
    info = '\x1b[4;30;42m'


class ProgressPercent(object):

    """
    Percent
    Example :
        Processing : [ 40%]
    """

    def __init__(self, max_value):
        """
        """
        self.value = 0
        self.__max_value = max_value
        self.__current_percent = 0

    def __repr__(self):
        """
        Provide the string according to the %
        """
        percent = "Processing: [{0}%]".format(self.__get_str_percent())
        return "{}{}{}".format(Colors.info, percent, Colors.reset)

    def __str__(self):
        """
        """
        return repr(self)

    def __get_str_percent(self):
        """
        """
        percent = str((self.get_percent() * 100))[0:4]
        return " " * (5 - len(percent)) + percent

    def get_percent(self):
        """
        """
        return round(self.value / float(self.__max_value), 1)


class ProgressDraw(object):
    def __init__(self, max_size):
        """
        """
        self.__max_size = max_size
        self.percent = 0

    def __get_block(self):
        """
        """
        if self.percent < 1:
            block = int(round(self.__max_size * self.percent))
        else:
            block = self.__max_size
        return block

    def __repr__(self):
        """
        """
        block = self.__get_block()
        return "{}{}{} ".format(
            ProgressTheme.beggining,
            ProgressTheme.done * block + ProgressTheme.not_done * (self.__max_size - block),
            ProgressTheme.end)
    def __str__(self):
        """
        """
        return repr(self)


class ElapseTime(object):
    def __init__(self):
        """
        """
        self.__start_time = None
        self.__update_time = None

    def start(self):
        """
        """
        self.__start_time = datetime.datetime.now().replace(microsecond=0)

    def __get_elapse(self):
        """This function provides elapse time between start() and now.

        self.__update_time-self.__start_time

        Args:
            None

        Returns:
            datetime object

        """
        self.__update_time = datetime.datetime.now().replace(microsecond=0)
        return (self.__update_time - self.__start_time)

    def __repr__(self):
        """
        """
        return str(self.__get_elapse())

    def __str__(self):
        """
        """
        return repr(self)


class SmoothProgressBar(object):

    """This Class provides a progressbar"""

    def __init__(self, debug=False):
        """Init the smoothProgressBar Class
        This function define attributes.

        Args:
            None

        Attributes:
            self.__interval (float) : refresh time
            self.__rows (float): screen size
            self.__columns (float): screen size
            self.__bar_length (int): progressbar size
            self.__description (str): task's description
            self.__is_running (bool)
            self.__percent (ProgressPercent)
            self.__draw (ProgressDraw)
            self.__elapse (ElapseTime)
            self.__timer (Timer): Thread

        Returns:
            obj

        """
        self.__timer = None
        self.__interval = 0.25
        if debug:
            self.__rows = 79
            self.__columns = 24
        else:
            self.__rows, self.__columns = os.popen(
                'stty size', 'r').read().split()

        self.__percent = None
        self.__draw = None
        self.__elapse = ElapseTime()

        self.__bar_length = int(0.50 * float(self.__columns))
        self.__description = None
        self.__is_running = False
        print("\n")
        os.system('setterm -cursor off')

    def __get_bar(self):
        """This function provides the string to print the progress and
        informations

        Args:
            None

        Returns:
            string: Processing: [ 100.%] [#########] 0:00:20 - task 10

        """
        bar_location = "\033[" + self.__rows + ";1H\r"
        current_progressbar = "{}{} {}{} - {}".format(
            bar_location,
            self.__percent,
            self.__draw,
            self.__elapse,
            self.__description
            )
        current_progressbar += ' ' * int(self.__columns)
        return current_progressbar[0:int(self.__columns)]

    def __isstarted(status=True):
        """
        Decorator to check progress bar status

        Args:
            func: decorated function
            status (bool): The expected value.

        Returns:
            func if self.__is_running = status

        """
        def tags_decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                """ wrapper """
                if self.__is_running is status:
                    return func(self, *args, **kwargs)
                return
            return wrapper
        return tags_decorator

    @__isstarted(True)
    def __refresh(self):
        """This function refresh the progress bar

        Call __get_bar(), print the string, call Timer functions to recall

        Args:
            None

        Returns:
            None

        """
        sys.stdout.write(self.__get_bar())
        sys.stdout.flush()
        self.__timer = Timer(self.__interval, self.__refresh)
        self.__timer.start()

    @__isstarted(False)
    def start(self, max_value):
        """This function start the progress bar

        Test if the progress is already running, set _startTime,
        call Timer functions to refresh

        Args:
            max_value (int): the value at 100%.

        Returns:
            None

        """
        self.__is_running = True
        self.__percent = ProgressPercent(max_value)
        self.__percent.value = 0
        self.__draw = ProgressDraw(self.__bar_length)
        self.__draw.percent = 0
        self.__elapse.start()
        self.__description = ProgressTheme.first_description
        self.__timer = Timer(self.__interval, self.__refresh)
        self.__timer.start()

    @__isstarted(True)
    def update(self, current_value, description=None):
        """This function update currentValue & description

        Args:
            current_value (int): current value
            description (string): current description

        Returns:
            None

        """
        self.__percent.value = current_value
        self.__draw.percent = self.__percent.get_percent()
        self.__description = description

    @__isstarted(True)
    def stop(self):
        """This function stop the progress bar.

        Args:
            None

        Results:
            None

        """
        self.__is_running = False
        self.__timer.cancel()
        print("\n")
        os.system('setterm -cursor on')
