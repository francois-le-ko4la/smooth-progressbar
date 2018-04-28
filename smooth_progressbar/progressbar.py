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

import os
import sys
from threading import Timer
import datetime
from functools import wraps


class ProgressTheme:
    refresh_time = 0.25
    done = '#'
    not_done = '.'
    separator = '-'
    beggining = '['
    end = ']'
    first_description = "Starting..."
    label_percentage = 'Processing:'
    size_elapse = 10
    size_description = 20


class Colors:
    reset = '\x1b[0m'
    info = '\x1b[4;30;42m'


class EscapeSequence:
    goback = '\r'
    linefeed = '\n'


class ProgressPercent(object):

    """
    Provides the percentage indicator
    Example :
        Processing : [ 40%]
    """

    def __init__(self, max_value):
        """
        Init the default values
        Take the max value to provide the percentage

        Args:
            max_value (int): value at 100%

        Returns:
            obj

        """
        self.value = 0
        self.__max_value = max_value
        self.__current_percent = 0

    def __repr__(self):
        """
        Provide the string according to the %

        Args:
            None

        Returns:
            str

        """
        return "{}{} {}{}%{}{}".format(Colors.info,
                                       ProgressTheme.label_percentage,
                                       ProgressTheme.beggining,
                                       self.__get_str_percent(),
                                       ProgressTheme.end,
                                       Colors.reset)

    def __str__(self):
        """
        Call repr

        Args:
            None

        Returns:
            repr result

        """
        return repr(self)

    def __get_str_percent(self):
        """
        Provide the percentage / string - fixed size

        Args:
            None

        Returns:
            str

        """
        percent = str((self.get_percent() * 100))[0:4]
        return " " * (5 - len(percent)) + percent

    def get_percent(self):
        """
        Calculates the percent value

        Args:
            None

        Returns:
            float

        """
        return round(self.value / float(self.__max_value), 1)


class ProgressDraw(object):

    def __init__(self, max_size):
        """
        Init the default value
        Take the max size (100%)

        Args:
            max_size (int): max size / 100%

        Returns:
            obj

        """
        self.__max_size = max_size
        self.percent = 0

    def __get_block(self):
        """
        Provides the number of block to print according to the progress

        Args:
            None

        Returns:
            int
        """
        if self.percent < 1:
            block = int(round(self.__max_size * self.percent))
        else:
            block = self.__max_size
        return block

    def __repr__(self):
        """
        Provides the string to print

        Args:
            None

        Returns:
            str
        """
        block = self.__get_block()
        return "{}{}{} ".format(
            ProgressTheme.beggining,
            ProgressTheme.done * block +
            ProgressTheme.not_done * (self.__max_size - block),
            ProgressTheme.end)

    def __str__(self):
        """
        call repr

        Args:
            None

        Returns:
            repr return
        """
        return repr(self)


class FixedSizeString(object):

    def __init__(self, max_size):
        self.value = ""
        self.max_size = max_size
        self.enable = True

    def __repr__(self):
        if self.enable is not True:
            return ' '
        current_value = self.value + ' ' * int(self.max_size)
        return Colors.reset + current_value[0:(int(self.max_size))]

    def __str__(self):
        """
        call repr

        Args:
            None

        Returns:
            repr return
        """
        return repr(self)


class ElapseTime(object):

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

    def __get_elapse(self):
        """
        This function provides elapse time between start() and now.

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
        Provides the string

        Args:
            None

        Returns:
            None

        """
        if self.enable is not True:
            return ""
        return str(self.__get_elapse())

    def __str__(self):
        """
        Call repr

        Args:
            None

        Returns:
            None

        """
        return repr(self)


class SmoothProgressBar(object):

    """This Class provides a progressbar"""

    def __init__(self, enable_elapse=True, enable_description=True):
        """
        Init the smoothProgressBar Class

        Args:
            None

        Attributes:
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

        self.__rows = None
        self.__columns = None
        self.__timer = None
        self.__percent = None
        self.__draw = None
        self.__isupdated = True
        self.__elapse = ElapseTime()
        self.__elapse.enable = enable_elapse
        self.__empty_line = FixedSizeString(80)
        self.__empty_line.value = ' '
        self.__description = FixedSizeString(ProgressTheme.size_description)
        self.__description.enable = enable_description
        self.__is_running = False
        self.__bar_length = self.__def_bar_lengh()

    def __def_bar_lengh(self):
        self.__rows, self.__columns = os.popen('stty size', 'r').read().split()
        self.__bar_length = int(self.__columns) - len(
            ProgressTheme.label_percentage) - 15
        if self.__elapse.enable:
            self.__bar_length = self.__bar_length - ProgressTheme.size_elapse
        if self.__description.enable:
            self.__bar_length = self.__bar_length - \
                ProgressTheme.size_description

        return self.__bar_length

    def __get_bar(self):
        """This function provides the string to print the progress and
        informations

        Args:
            None

        Returns:
            string: Processing: [ 100.%] [#########] 0:00:20 - task 10

        """
        current_progressbar = FixedSizeString(int(self.__columns) + 14)
        current_progressbar.value = "{}{} {}{} {}".format(
            '\r',
            self.__percent,
            self.__draw,
            self.__elapse,
            self.__description
        )
        return str(current_progressbar)

    def __get_log(self):
        """
        """
        empty_line = FixedSizeString(int(self.__columns))
        empty_line.value = ' '
        if self.__description.enable is not True:
            self.__description.enable = True
            self.__description.max_size = self.__columns
            log = "\r" + \
                str(empty_line) + "\r" + str(self.__description) + "\n"
            self.__description.enable = False
            return log
        return ""

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

    def __clean_progress(self):
        empty_line = FixedSizeString(int(self.__columns))
        empty_line.value = ' '
        sys.stdout.write("\r" + str(empty_line) + "\r")
        sys.stdout.flush()

    @__isstarted(True)
    def __refresh(self):
        """This function refresh the progress bar

        Call __get_bar(), print the string, call Timer functions to recall

        Args:
            None

        Returns:
            None

        """
        if self.__isupdated:
            self.__isupdated = False
            self.__draw.max_size = self.__def_bar_lengh()
            sys.stdout.write(self.__get_log())
            sys.stdout.write(self.__get_bar())
            sys.stdout.flush()
        self.__timer = Timer(ProgressTheme.refresh_time, self.__refresh)
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
        self.__description.value = ProgressTheme.first_description
        self.__timer = Timer(ProgressTheme.refresh_time, self.__refresh)
        self.__timer.start()
        self.__isupdated = True

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
        self.__description.value = description
        self.__isupdated = True

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
        self.__clean_progress()
