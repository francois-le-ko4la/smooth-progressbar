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
from smooth_progressbar import SmoothProgressBar
import unittest


class TestProgressBar(unittest.TestCase):
    def test_progressbar(self):
        """ Test
        """
        my_progressbar = SmoothProgressBar(debug=True)
        my_progressbar.start(10)

        for i in range(1, 11):
            my_progressbar.update(i, "task "+str(i))
            time.sleep(2)
        my_progressbar.stop()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
