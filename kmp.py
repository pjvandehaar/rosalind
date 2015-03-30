#!/usr/bin/env python3

import sys
from Bio import SeqIO
seqs = list(str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))
seq = seqs[0]

P = list(None for i in range(1+len(seq)))

P[1] = 0

for k in range(2,len(seq)+1):
    for j in range(P[k-1]+1,0, -1):
        if seq[0:j] == seq[k-j:k]:
            P[k] = j
            break
        else:
            P[k] = 0

print(*P[1:])
