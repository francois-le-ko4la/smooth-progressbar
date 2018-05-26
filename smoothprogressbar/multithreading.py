#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

#######
   #     #    #  #####   ######    ##    #####
   #     #    #  #    #  #        #  #   #    #
   #     ######  #    #  #####   #    #  #    #
   #     #    #  #####   #       ######  #    #
   #     #    #  #   #   #       #    #  #    #
   #     #    #  #    #  ######  #    #  #####

"""

from threading import Thread, Timer


class MultiThread(Thread):
    """
    A class that represents a thread of control.
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
    def __init__(self, func, elapse):
        Thread.__init__(self)
        self.__running = True
        self.__timer = None
        self.__func = func
        self.__elapse = elapse
        self.setDaemon(True)

    @property
    def func(self):
        """
        Returns the callable object defined by Thread constructor.

        Args:
            None.

        Returns:
            callable object
        """
        return self.__func

    def run(self):
        """
        Method (override) representing the thread's activity.
        This method will raise a RuntimeError if called more than once on the
        same thread object.

        Args:
            None.

        Returns:
            None.
        """
        if not self._initialized:
            raise RuntimeError("thread.__init__() not called")

        self.__func()
        if self.__running:
            self.__timer = Timer(self.__elapse, self.run)
            self.__timer.start()

    def stop(self):
        """
        Wait until the thread terminates.
        This blocks the calling thread until the thread whose join() method is
        called terminates -- either normally or through an unhandled exception.

        Args:
            None.

        Returns:
            None.
        """
        self.__running = False
        self.__timer.cancel()
        self.join()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
