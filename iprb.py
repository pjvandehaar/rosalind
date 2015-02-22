#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/hamm/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

import itertools
k,m,n = (int(s) for s in input().split())

'''
crosses:
DD, DH, DR: 100%
HH: 75%
HR: 50%
RR: 0%
'''

from math import factorial as fac
def choose(n,r):
    return fac(n)/fac(r)/fac(n-r)

print( (choose(k,2) + k*m + k*n + choose(m,2)*0.75 + m*n*0.5)/choose(k+m+n,2) )
