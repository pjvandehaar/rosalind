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
==
+ ignore "trivials" (0,1,4,5 of one character)
+ ignore repeats?
'''

def binarize_character(ch):
    return list(int(elem == ch[0]) for elem in ch)

from sys import stdin
lines = stdin.readlines()
characters = zip(*lines)
characters = list(binarize_character(ch) for ch in characters)

for ch in characters:
    if 1 < sum(ch) < len(ch)-1:
        print(''.join(map(str, ch)))
        
