#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

import sys
lines = sys.stdin.readlines()

print(sum(a!=b for a,b in zip(lines[0],lines[1])))
