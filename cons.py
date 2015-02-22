#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''

import sys
from Bio import SeqIO

seqs = list(record.seq for record in SeqIO.parse(sys.stdin, 'fasta'))

loci_lists = list(zip(*seqs))

## for each loci, the freqency of each base
loci_freqs = list(dict((base,loci_list.count(base)) for base in 'ACTG') for loci_list in loci_lists)

concensus_seq = ''.join(max(loci_freq, key=loci_freq.get) for loci_freq in loci_freqs)
print(concensus_seq)

for base in 'ACGT':
    print('{}: {}'.format(base, ' '.join(str(loci_freq[base]) for loci_freq in loci_freqs)))
