#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:24:09 2018

@author: toddbilsborough
"""

# Just a direct copy of your solution from C#
# Miserable at 14s

factors = []
abundant = []
is_abundant_sum = []

limit = 28123

factors = list([] for i in range(0, limit + 1))
is_abundant_sum = list(False for i in range(0, limit + 1))

def get_factors(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            if d not in factors[n]: factors[n].append(d)
            if n // d not in factors[n]: factors[n].append(n // d)
        d += 1
    factors[n].append(1)
    
for i in range(1, limit + 1): 
    get_factors(i)
    if sum(factors[i]) > i: abundant.append(i)
    
for n in [a + b for a in abundant for b in abundant]:
    if n <= limit:
        is_abundant_sum[n] = True

s = 0

for n in range(1, limit + 1):
    if is_abundant_sum[n] == False:
        s += n