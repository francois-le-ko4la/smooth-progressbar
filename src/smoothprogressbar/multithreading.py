#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Manage multithreading.

It defines a class called MultiThread which is a subclass of the built-in
class Timer/threading. The class provides a run method that implements the
activity of the thread, which can be defined by passing a callable object to
the constructor. The stop method is used to stop the multithreading.
The func property returns the callable object defined in the constructor.
"""

from __future__ import annotations

from threading import Timer


class MultiThread(Timer):
    """A class that represents a thread of control.

    This is used to refresh the network node regurarly. (self.__refresh())
    This class subclassed Thread class :

    We specify the activity by passing a callable object to the constructor.

    Example:
        >>> import time
        >>> def mytask(): print("lorem ipsum dolor sit amet consectetur")
        >>> mthr = MultiThread(0.1, mytask)
        >>> mthr.start() ; time.sleep(0.25);print("other task") ; mthr.stop()
        lorem ipsum dolor sit amet consectetur
        lorem ipsum dolor sit amet consectetur
        other task
    """

    def run(self) -> None:
        """Do tasks.

        Method (override) representing the thread's activity.
        This method will raise a RuntimeError if called more than once on the
        same thread object.

        Returns:
            None.
        """
        while not self.finished.wait(self.interval):
            self.function()

    def stop(self) -> None:
        """Stop the Timer."""
        self.cancel()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
