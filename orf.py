#!/usr/bin/env python3

complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
def get_reverse_complement(seq):
    return ''.join(complement[base] for base in reversed(seq))

assert get_reverse_complement('AAATCG') == 'CGATTT'


codon_text = '''
TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G
'''.strip()
def pairwise(lst):
    it = iter(lst)
    return list(zip(it, it))
codons = {codon: prot for codon, prot in pairwise(codon_text.split())}

def get_all_orfs(seq):
    for seq in (seq, get_reverse_complement(seq)):
        for start in range(len(seq)-2): # -2 b/c codon needs three bases.
            if codons[seq[start:start+3]] == 'M':
                rv = 'M'
                for pos in range(start+3, len(seq)-2, 3):
                    prot = codons[seq[pos:pos+3]]
                    if prot == 'Stop':
                        yield rv
                        break
                    else:
                        rv += prot

assert sorted(set(get_all_orfs('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'))) == sorted([
    'MLLGSFRLIPKETLIQVAGSSPCNLS',
    'M',
    'MGMTPRLGLESLLE',
    'MTPRLGLESLLE'
])


if __name__ == '__main__':
    with open('orf.txt') as f:
        seq = ''.join([line.strip() for line in f.readlines() if not line.startswith('>')])

    for orf in sorted(set(get_all_orfs(seq))):
        print(orf)
