#!/usr/bin/env python3

s = '''
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''
import re
aa_masses = {key:float(val) for key,val in re.findall('([A-Z])   ([0-9]+\.[0-9]+)', s)}

import sys
ion_masses = list(float(line) for line in sys.stdin.readlines())
masses = list(b-a for a,b in zip(ion_masses, ion_masses[1:]))
def get_closest_aa(mass):
    distances = ((abs(mass-aa_mass), aa_code) for aa_code,aa_mass in aa_masses.items())
    return min(distances)[1]
assert get_closest_aa(163) == 'Y'
assert get_closest_aa(164) == 'Y'
assert get_closest_aa(0) == 'G'

print(''.join(get_closest_aa(mass) for mass in masses))
