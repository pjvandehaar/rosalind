#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
'''

import sys
from Bio import SeqIO
seqs = {record.id: record.seq for record in SeqIO.parse(sys.stdin, 'fasta')}

from itertools import permutations
for a,b in permutations(seqs, 2):
    if str(seqs[a][-3:]) == str(seqs[b][:3]):
        print(a, b)
