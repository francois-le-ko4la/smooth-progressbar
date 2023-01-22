#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module manage multithreading."""
from __future__ import annotations

from threading import Thread, Timer
from typing import Callable


class MultiThread(Thread):
    """
    A class that represents a thread of control.

    This is used to refresh the progressbar regurarly. (self.__refresh())
    This class subclassed Thread class :
        class Thread(builtins.object)

    We specify the activity by passing a callable object to the constructor.

    Use:
        >>> import time
        >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
        >>> mthr = MultiThread(mytask, 0.1)
        >>> mthr.start() ; print("other task");time.sleep(0.3) ; mthr.stop()
        lorem ipsum dolor sit amet consectetur
        other task
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur

    """

    __timer: Timer

    def __init__(self, func: Callable[[], None], elapse: float) -> None:
        """Init."""
        Thread.__init__(self)
        self.__running = True
        self.__func: Callable[[], None] = func
        self.__elapse: float = elapse

    @property
    def func(self) -> Callable[[], None]:
        """Get func.

        Returns the callable object defined by Thread constructor.

        Returns:
            Callable[[], None]: callable object
        """
        return self.__func

    def run(self) -> None:
        """Do tasks.

        Method (override) representing the thread's activity.
        This method will raise a RuntimeError if called more than once on the
        same thread object.

        Returns:
            None.
        """
        self.__func()
        if self.__running:
            self.__timer = Timer(self.__elapse, self.run)
            self.__timer.start()

    def stop(self) -> None:
        """Stop multithreading.

        Wait until the thread terminates.
        This blocks the calling thread until the thread whose join() method is
        called terminates -- either normally or through an unhandled exception.

        Returns:
            None.
        """
        self.__running = False
        self.__timer.cancel()
        self.join()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
