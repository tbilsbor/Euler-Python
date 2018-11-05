#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:14:24 2018

@author: toddbilsborough
"""

# Standard bootstrapper runs in 12.9 ms
# Here's a modification based on refinements
# Runs in 609 ms; bootstrapper wins

from math import sqrt

def is_prime(n):
    if n == 1: return False
    if n < 4: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(sqrt(n))
    for f in range(5, r + 1):
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

primes = [2]
p = 3
while len(primes) < 10001:
    if is_prime(p):
        primes.append(p)
    p += 2
    
#print(primes[10000])