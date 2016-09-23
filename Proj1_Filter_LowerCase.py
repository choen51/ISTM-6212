#!/usr/bin/env python

"""
Problem 3, Part A
A filter that transform words into lower case.
"""

import fileinput


def process(line):
    """Re-format each line of input into lower case."""
    print(line.lower())


for line in fileinput.input():
    process(line)
