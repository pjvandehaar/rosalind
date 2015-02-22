#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/splc

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

import sys
from Bio import SeqIO, Seq
seqs = (str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))

full_seq = next(seqs)

for seq in seqs:
    full_seq = full_seq.replace(seq, '')
print(Seq.Seq(full_seq).translate().rstrip('*'))
