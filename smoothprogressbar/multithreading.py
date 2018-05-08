#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from threading import Timer
from threading import Thread
import time


class MultiThread(Thread):
    """
    Use:
        >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
        >>> mthr = MultiThread(mytask, 0.25)
        >>> mthr.start() ; print("other task");time.sleep(1) ; mthr.stop()
        lorem ipsum dolor sit amet consectetur
        other task
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur

    """
    def __init__(self, func, elapse):
        Thread.__init__(self)
        self.__running = True
        self.__func = func
        self.__elapse = elapse

    @property
    def func(self):
        return self.__func

    def run(self):
        self.__func()
        if self.__running:
            time.sleep(self.__elapse)
            self.run()

    def stop(self):
        self.__running = False
        self.join()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
