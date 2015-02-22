#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/edit

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t).  An edit is the substitution, insertion, or deletion of a single character.
'''

import sys
from Bio import SeqIO
s, t = (str(record.seq) for record in SeqIO.parse(sys.stdin, 'fasta'))

'edit[t_len, s_len] = the edit_distance between t[:t_len] and s[:s_len]'
try:
    import numpy
except ImportError:
    edit = {}
else:
    edit = numpy.empty((len(t)+1,len(s)+1), dtype=int)

for s_len in range(len(s)+1):
    for t_len in range(len(t)+1):
        if t_len == 0 or s_len == 0: # one string is empty
            result = t_len + s_len
        elif t[t_len-1] == s[s_len-1]: # last char is identical
            result = edit[t_len-1, s_len-1]
        else: # insert, delete, or substitute - whichever gives the best value
            result = 1+min(
                edit[t_len-1, s_len],
                edit[t_len-1, s_len-1],
                edit[t_len, s_len-1])
        edit[t_len, s_len] = result

print(edit[len(t), len(s)])

# trace back through the table to find a path that the lowest values followed
trace = [(len(t), len(s))]
while trace[-1] != (0,0):
    x, y = trace[-1][0], trace[-1][1]
    if x == 0:
        trace.append((x, y-1))
    if y == 0:
        trace.append((x-1, y))
    else:
        parents = [(x-1,y-1), (x-1,y), (x,y-1)]
        min_parent = min(parents, key=edit.__getitem__)
        trace.append(min_parent)

trace.reverse()
trace = list(zip(*trace))
# trace is like [[0,1,2,3,3,4], [0,1,1,2,3,3]]

changed = list(cur!=next for cur,next in zip(trace[1][:-1], trace[1][1:]))
print(''.join(s[pos] if changed else '-' for pos,changed in zip(trace[1], changed)))

changed = list(cur!=next for cur,next in zip(trace[0][:-1], trace[0][1:]))
print(''.join(t[pos] if changed else '-' for pos,changed in zip(trace[0], changed)))
