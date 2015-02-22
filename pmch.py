#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/grph/

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
'''

import sys
from Bio import SeqIO
seq = str(list(SeqIO.parse(sys.stdin, 'fasta'))[0].seq)

from math import factorial as fac

print(fac(seq.count('U')) * fac(seq.count('G')))
