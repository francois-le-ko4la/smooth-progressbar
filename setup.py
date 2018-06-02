#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.

"""
from setuptools import setup
from setuptools.config import read_configuration
import warnings
import sys


if not sys.version_info[0] == 3:
            sys.exit("Sorry, your Python is not supported (yet)")

warnings.filterwarnings("ignore")

CFG = read_configuration('./setup.cfg')
CFG["options"].update(CFG["metadata"])
CFG = CFG["options"]
setup(use_scm_version=False, **CFG)
