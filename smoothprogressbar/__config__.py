#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

  ####    ####   #    #  ######     #     ####
 #    #  #    #  ##   #  #          #    #    #
 #       #    #  # #  #  #####      #    #
 #       #    #  #  # #  #          #    #  ###
 #    #  #    #  #   ##  #          #    #    #
  ####    ####   #    #  #          #     ####

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
