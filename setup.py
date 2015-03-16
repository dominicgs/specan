#!/usr/bin/env python
"""
Specan setup

Install script for the Specan spectrum analyzer tool

Usage: python setup.py install

This file is part of Specan
Copyright 2012 Dominic Spill
"""

from distutils.core import setup

setup(
    name        = "specan",
    description = "A tool for reading spectrum analyzer data from Ubertooth or other RF dongles",
    author      = "Jared Boone, Michael Ossmann, Dominic Spill",
    url         = "https://github.com/dominicgs/specan/",
    license     = "GPL",
    version     = '',
    packages    = ['specan'],
    scripts     = ['specan-ui'],
    classifiers=[
        'Development Status :: 5 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)
