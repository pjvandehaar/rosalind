#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/ini6

Given: A string s of length at most 10000 letters.

Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.
'''

import sys

with open(sys.argv[1], 'r') as f:
    for line_number, line in enumerate(f):
        if 1 == line_number % 2:
            print(line.rstrip('\n'))

## if you want the output in a file, you're gonna have to pipe it yourself.
