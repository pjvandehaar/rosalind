#!/usr/bin/env python3

from sys import stdin, stdout
from Bio import Phylo
clades = list(Phylo.BaseTree.Clade(name=name) for name in stdin.readline().split())
splits = list(list(int(c) for c in line.strip()) for line in stdin.readlines())

def find_cols_to_unify(splits):
    for split in splits:
        if 2 == sum(split):
            return tuple(i for i,x in enumerate(split) if x == 1)
        elif len(split)-2 == sum(split):
            return tuple(i for i,x in enumerate(split) if x == 0)
    raise Exception('no cols to unify!', splits)

def print_splits(splits):
    for split in splits:
        print(split)

def print_clades(clades):
    for clade in clades:
        tree = Phylo.BaseTree.Tree.from_clade(clade)
        Phylo.write(tree, stdout, 'newick', plain=True)

while 0 < len(splits):
    print('===Vv')

    print_clades(clades)
    print_splits(splits)

    col1, col2 = find_cols_to_unify(splits)
    print('match cols ', col1, col2)

    # remove the second of the unified columns
    for split in splits:
        split.pop(col2)
    # remove all trivial splits
    splits = list(split for split in splits if sum(split) > 1 and sum(split)+1 < len(split))

    # unify the clades
    clades[col1] = Phylo.BaseTree.Clade(clades=[clades[col1], clades[col2]])
    clades.pop(col2)

    print('===A^')

final_clade = Phylo.BaseTree.Clade(clades=clades)
print_clades([final_clade])
