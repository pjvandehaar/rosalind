#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/prot/

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''

strand = input()
pattern = input()

import re
print(' '.join(str(1+match.start()) for match in re.finditer('(?=(%s))'%pattern.strip(), strand)))
