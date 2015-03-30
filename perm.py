#!/usr/bin/env python3

n = int(input())

from math import factorial
print(factorial(n))

from itertools import permutations
for t in permutations(range(1,1+n)):
    print(*t)
