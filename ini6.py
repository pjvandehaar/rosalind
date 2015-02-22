#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/ini6

Given: A string s of length at most 10000 letters.

Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.
'''

import sys
import mmap
import re
import collections

with open(sys.argv[1], 'rb') as f:
    # mmap makes a buffer. Then re can process the file as a stream rather than one big string.
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:  
        word_counts = collections.Counter(match.group(0) for match in re.finditer(b'[A-Za-z]+', mm))
for word, count in word_counts.items():
    print(word.decode(), count)
