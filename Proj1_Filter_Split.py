#!/usr/bin/env python

"""
Problem 3, Part A
A filter that transforms a set of text into a word per line.
"""

import fileinput
import re

def process(lines):
    """Split input text into lines"""
    line = re.split('[\W,2]+',lines)
    
    """Split the lines further into words (Any whitespaces are excluded.)"""
    for word in line: 
        if word.strip():
            print(word)
        
    
for lines in fileinput.input():
    process(lines)