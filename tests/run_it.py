#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import time
from smoothprogressbar.prgbr import SmoothProgressBar


my_progressbar = SmoothProgressBar()
my_progressbar.start(3)
for i in range(1, 4):
    my_progressbar.update(i-1, "task {} in progress...".format(str(i)))
    time.sleep(1)
    # ....
    my_progressbar.update(i, "task {} finished...".format(str(i)))
    time.sleep(1)
my_progressbar.stop()


my_progressbar = SmoothProgressBar(enable_elapse=False)
my_progressbar.start(3)
for i in range(1, 4):
    my_progressbar.update(i-1, "task {} in progress...".format(str(i)))
    time.sleep(1)
    # ....
    my_progressbar.update(i, "task {} finished...".format(str(i)))
    time.sleep(1)
my_progressbar.stop()

my_progressbar = SmoothProgressBar(enable_msg=False)
my_progressbar.start(3)
for i in range(1, 4):
    my_progressbar.update(i-1, "task {} in progress...".format(str(i)))
    time.sleep(1)
    # ....
    my_progressbar.update(i, "task {} finished...".format(str(i)))
    time.sleep(1)
my_progressbar.stop()


my_progressbar = SmoothProgressBar(enable_elapse=False,
                                   enable_msg=False)
my_progressbar.start(3)
for i in range(1, 4):
    my_progressbar.update(i-1, "task {} in progress...".format(str(i)))
    time.sleep(1)
    my_progressbar.msg = "ouuuups error 1/1...."
    time.sleep(1)
    my_progressbar.msg = "ouuuups warning 1/2...."
    time.sleep(0.25)
    my_progressbar.msg = "ouuuups warning 2/2...."
    # ....
    my_progressbar.update(i, "task {} finished...".format(str(i)))
    time.sleep(2)
my_progressbar.stop()
