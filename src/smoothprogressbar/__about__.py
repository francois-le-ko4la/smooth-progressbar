#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define about.

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # type: ignore

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")

__pkg_name__ = "smoothprogressbar"
__version__: str = metadata.version(__pkg_name__)
__author__: str = metadata.metadata(__pkg_name__)["Author"]
__url__: str = metadata.metadata(__pkg_name__)["Project-URL"]
__license__: str = metadata.metadata(__pkg_name__)["License"]
__description__: str = metadata.metadata(__pkg_name__)["Summary"]
