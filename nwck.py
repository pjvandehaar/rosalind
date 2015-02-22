#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/nwck

Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
'''

from Bio import Phylo
import io
import sys

def padded_pairs(l):
    '''[1,2,3,4,5,6] => [(1,2), (4,5)]'''
    itr = iter(l)
    while True:
        yield (next(itr), next(itr))
        next(itr)

with sys.stdin as f:
    for tree_string, nodes in padded_pairs(f.readlines()):
        tree = Phylo.read(io.StringIO(tree_string), 'newick')
        node1, node2 = nodes.split()
        print(int(tree.distance(node1, node2)), end=' ')
