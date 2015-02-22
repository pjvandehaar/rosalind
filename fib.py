#!/usr/bin/env python3
'''
author: pjv9
problem: http://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

nmonths,k = (int(s) for s in input().split())

nadults = 0
nbabies = 1

for month in range(nmonths):
    nbabies, nadults = nadults * k, nadults + nbabies

print(nadults)
