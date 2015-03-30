#!/usr/bin/env python3

'''
ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC
=>
10110 -
10100 -
10000
10111
11011
11101
00001
11111
'''

from sys import stdin
lines = stdin.readlines()

for ch in zip(*lines):
    binary = list(int(elem==ch[0]) for elem in ch)
    if 1 < sum(binary) < len(binary)-1:
        print(*binary, sep='')
