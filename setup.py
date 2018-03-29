#!/usr/bin/env python3
"""A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.
    pylint has been used :
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Note:
    This script is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 3 of the License, or (at your option) any later version.

    This script is provided in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

from setuptools import setup


def readme():
    """This function provides the readme file.
    """
    with open('README.md') as read_me:
        return read_me.read()


setup(
    name='smooth-progressbar',
    version='0.1',
    description='The funniest progress bar over the world',
    long_description=readme(),
    python_requires='>=3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3.6',
        'Topic :: REST API :: Social Network / Cloud',
        ],
    url='https://github.com/francois-le-ko4la/smooth-progressbar',
    author='Ko4lA',
    author_email='francois@le.ko4la.fr',
    license='',
    packages=['smooth_progressbar'],
    zip_safe=False
    )