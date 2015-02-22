#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/lcsq

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The longest common subsequence
'''

import sys
from Bio import SeqIO
s, t = (str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))

import collections
Node = collections.namedtuple('Node', 'com parent'.split())
'common[t_index, s_index] = Node(com=common_subseq_length(t[:t_index], s[:s_index]), parent_index)'
common = {}

for s_i in range(len(s)+1):
    for t_i in range(len(t)+1):
        if s_i == 0:
            result = Node(parent=(s_i, t_i-1), com=0)
        elif t_i == 0:
            result = Node(parent=(s_i-1, t_i), com=0)
        elif s[s_i-1] == t[t_i-1]: # last char is identical
            result = Node(parent=(s_i-1, t_i-1), com=1+common[s_i-1, t_i-1].com)
        else:
            parent_indexes = [
                (s_i-1, t_i-1),
                (s_i-1, t_i),
                (s_i, t_i-1)
            ]
            best_parent_index = max(parent_indexes, key=(lambda p:common[p].com))
            result = Node(parent=best_parent_index, com=common[best_parent_index].com)
        common[s_i, t_i] = result

'trace back through, recording the characters that were common'
common_chars = []
while s_i and t_i:
    if s[s_i-1] == t[t_i-1]:
        common_chars.insert(0, s[s_i-1])
    s_i, t_i = common[s_i,t_i].parent

print(''.join(common_chars))
