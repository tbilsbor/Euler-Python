#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:14:06 2018

@author: toddbilsborough
"""

# Dynamic programming solution
# Considerably worse at 200ms, but not a great implementation

from math import sqrt

limit = 10000

factors = [[1] for i in range(0, limit)]

def get_factors(n):
    start = int(sqrt(n))
    for d in range(start, 1, -1):
        if d in factors[n]: continue
        if n % d == 0:
            factors[n].append(d)
            if d ** 2 != n: factors[n].append(n // d)
            if len(factors[d]) > 1:
                for factor in factors[d]:
                    if factor not in factors[n]: factors[n].append(factor)
                    if n // factor not in factors[n] and factor != 1: 
                        factors[n].append(n // factor)

for n in range(2, limit):
    get_factors(n)
    
sums = [sum(factors[i]) for i in range(0, limit)]
total = 0
for a in range(0, limit):
    b = sums[a]
    if b < limit:
        if sums[a] == b and sums[b] == a and a != b:
            total += sums[a]