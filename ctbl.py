#!/usr/bin/env python3

from Bio import Phylo

tree = next(Phylo.parse('rosalind_ctbl.txt', 'newick'))
all_terminals = sorted(terminal.name for terminal in tree.get_terminals())

for clade in tree.depths():
    if 1 < clade.count_terminals() < tree.count_terminals() - 1:
        clade_terminals = set(terminal.name for terminal in clade.get_terminals())
        for terminal in all_terminals:
            print(1 if terminal in clade_terminals else 0, end='')
        print('')
