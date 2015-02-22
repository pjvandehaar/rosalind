#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

strand = input()

for a,b in ['AT','CG']:
    strand = strand.replace(a,'~').replace(b,a).replace('~',b)
print(''.join(reversed(strand)))
