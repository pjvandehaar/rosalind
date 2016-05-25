#!/usr/bin/env python3

import sys
import requests
import re

def get_n_glycosylation_indexes(seq):
    matches = re.finditer(r'(?=N[^P][ST][^P])', seq) # Use a lookahead to catch overlapping matches
    return [1 + m.start() for m in matches] # dunno why the +1
assert get_n_glycosylation_indexes('MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK') == [85, 118, 142, 306, 395]

def fetch_seq(prot_id):
    r = requests.get('http://www.uniprot.org/uniprot/{}.fasta'.format(prot_id))
    r.raise_for_status()
    text_lines = [line.strip() for line in r.content.decode('ascii').split('\n')]
    assert len([line for line in text_lines if line.startswith('>')]) == 1
    seq = ''.join(line for line in text_lines if not line.startswith('>'))
    assert all(aa in 'ACDEFGHIKLMNPQRSTVWY' for aa in seq)
    return seq

prot_ids = [line.strip() for line in sys.stdin.readlines() if line.strip()]

for prot_id in prot_ids:
    seq = fetch_seq(prot_id)
    n_gly_indexes = get_n_glycosylation_indexes(seq)
    if n_gly_indexes:
        print(prot_id)
        print(' '.join(str(index) for index in n_gly_indexes))
