#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/lcsm

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''

def common_seq_of_length(seq_length):
    for start_pos in range(0, len(s)-seq_length+1):
        if all(-1 != seq.find(s[start_pos:start_pos+seq_length]) for seq in seqs):
            return s[start_pos:start_pos+seq_length]
    return None

# bisect the longest seq_length that doesn't give None.
lo, hi = 0, len(s)
while lo < hi:
    mid = (lo+hi)//2+1
    result = common_seq_of_length(mid)
    if result is None:
        hi = mid-1
    else:
        longest_common_seq = result
        lo = mid
print(longest_common_seq)
