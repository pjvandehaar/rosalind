#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/dna/
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

print(*map(input().count, "ACGT"))
