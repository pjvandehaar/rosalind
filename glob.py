#!/usr/bin/env python3

import sys
from Bio import SeqIO

seqs = list(str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
print(int(pairwise2.align.globalds(seqs[0], seqs[1], MatrixInfo.blosum62, -5, -5)[0][2]))
