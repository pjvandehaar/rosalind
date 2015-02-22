#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

import sys
from Bio import SeqIO

seqs = ({'id':record.id, 'gc':sum(record.seq.count(l) for l in 'GC') / sum(record.seq.count(l) for l in 'ACTG')} for record in SeqIO.parse(sys.stdin, 'fasta'))

best_seq = max(seqs, key=lambda x: x['gc'])
print(best_seq['id'])
print(best_seq['gc']*100)


