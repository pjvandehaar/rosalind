#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''

codestring = '''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''
import re
codes = dict(re.findall('([AUCG]{3}) ([A-Z][a-z]*)', codestring))
from collections import Counter
num_seqs_for_aa = Counter(codes.values())

def get_num_seqs(prot_seq):
    num_seqs = num_seqs_for_aa['Stop']
    for aa in prot_seq:
        num_seqs *= num_seqs_for_aa[aa]
    return num_seqs % 1000000


prot_seq = input()
print(get_num_seqs(prot_seq))
