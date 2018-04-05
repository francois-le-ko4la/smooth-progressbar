#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from threading import Timer
import datetime


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
            self.__text (str): text to print
            self.__bar_length (int): progressbar size
            self.__start_time (datetime): start time
            self.__update_time (datetime): update time
            self.__max_value (int): maximum value (100%)
            self.__description (str):
            self.__current_value (int):
            self.__current_percent (float)
            self.__is_running (bool)
            self.__is_updated (bool)
            self.__previous_percent (str)

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
        self.__text = None
        self.__bar_length = int(0.30 * float(self.__columns))
        self.__filled_length = None
        self.__start_time = None
        self.__update_time = None
        self.__max_value = None
        self.__description = None
        self.__current_value = None
        self.__current_percent = None
        self.__is_running = False
        self.__is_updated = False
        self.__previous_percent = ""
        print("\n")
        os.system('setterm -cursor off')

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

    def __set_percent(self):
        """This function provides current percent.

        current_percent=round(self.__current_value/float(self.__max_value), 1)

        Args:
            None

        Returns:
            None

        """
        self.__current_percent = round(
            self.__current_value / float(self.__max_value), 1)

    def __get_infosbar(self):
        """This function provides an information to print.

        Provides : Elapse and description.

        Args:
            None

        Returns:
            string: "{elapse} | {description}"

        """
        return "{0} | {1}".format(
            self.__get_elapse(),
            self.__description)

    def __get_percentbar(self):
        """This function provides the string to print the progress

        Provides progress and bar according to the screen size.

        Args:
            None

        Returns:
            string: Processing (70.0%): |///////////////     |

        """
        if self.__current_percent < 1:
            block = int(round(self.__bar_length * self.__current_percent))
        else:
            block = self.__bar_length
        return "\033[" + self.__rows + ";1H\rProcessing ({0}%): |{1}| ".format(
            str((self.__current_percent * 100))[0:4],
            "/" * block + " " * (self.__bar_length - block))

    def __get_bar(self):
        """This function provides the string to print the progress and
        informations

        Call __get_percentbar(), self.__get_infosbar and provides a complete
        progress bar

        Args:
            None

        Returns:
            string: Processing (70.0%): |///////////////     | 0:00:01 | task 1

        """
        if self.__is_updated:
            self.__previous_percent = self.__get_percentbar()
            self.__is_updated = False
        new_progressbar = ""
        new_progressbar += self.__previous_percent
        new_progressbar += self.__get_infosbar()
        new_progressbar += ' ' * int(self.__columns)
        return new_progressbar[0:int(self.__columns)]

    def __refresh(self):
        """This function refresh the progress bar

        Call __get_bar(), print the string, call Timer functions to recall

        Args:
            None

        Returns:
            None

        """
        if self.__current_value is not None:
            sys.stdout.write(self.__get_bar())
            sys.stdout.flush()
        if self.__is_running:
            self.__timer = Timer(self.__interval, self.__refresh)
            self.__timer.start()

    def start(self, max_value):
        """This function start the progress bar

        Test if the progress is already running, set _startTime,
        call Timer functions to refresh

        Args:
            max_value (int): the value at 100%.

        Returns:
            None

        """
        if self.__is_running is not True:
            self.__is_running = True
            self.__max_value = max_value
            self.__start_time = datetime.datetime.now().replace(microsecond=0)
            self.__timer = Timer(self.__interval, self.__refresh)
            self.__timer.start()

    def update(self, current_value, description=None):
        """This function update currentValue, description, __update_time
        and call __set_percent().

        Args:
            current_value (int): current value
            description (string): current description

        Returns:
            None

        """
        self.__current_value = current_value
        self.__description = description
        self.__update_time = time.time()
        self.__set_percent()
        self.__is_updated = True

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
