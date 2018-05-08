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

class ProgressTheme:
    refresh_time = 0.25
    done = '#'
    not_done = '.'
    separator = '-'
    beggining = '['
    end = ']'
    first_description = "Starting..."
    label = 'Processing: '
    size_elapse = 10
    size_description = 20


class Color:
    reset = '\x1b[0m'
    info = '\x1b[4;30;42m'


class EscapeSequence:
    goback = '\r'
    linefeed = '\n'
