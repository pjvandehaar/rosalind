#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/sseq

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''

import sys
from Bio import SeqIO
seq, sseq = (str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))

for i, char in enumerate(seq):
    if sseq[0] == char:
        sseq = sseq[1:]
        print(i+1, end=' ')
        if not sseq:
            break
