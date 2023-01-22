#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define config."""

from __future__ import annotations

from enum import Enum, unique


@unique
class Theme(Enum):
    """Define constants."""

    REFRESH_TIME: float = 0.1
    DONE: str = '#'
    NOT_DONE: str = '.'
    BEG: str = '['
    END: str = ']'
    FIRST_DESCRIPTION: str = 'Starting...'
    LABEL: str = 'Processing: '
    RESET: str = '\x1b[0m'
    INFO: str = '\x1b[4;30;42m'
    TAB: str = '\t'
    GOBACK: str = '\r'
    LINEFEED: str = '\n'
