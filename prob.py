#!/usr/bin/env python3

import sys
from math import log10

seq = input()
gcs = list(float(x) for x in input().split())

acgt_freqs = list(seq.count(letter) for letter in 'ACGT')
gc_freq = sum(acgt_freqs[1:3])
at_freq = sum(acgt_freqs) - gc_freq

def likelihood(gc):
    #return log(gc**gc_freq * (1-gc)**at_freq)
    return gc_freq * log10(gc/2) + at_freq*log10((1-gc)/2)

print(*('{:.3f}'.format(likelihood(gc)) for gc in gcs))
