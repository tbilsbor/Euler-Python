#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:00:08 2018

@author: toddbilsborough
"""

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
# in its decimal fraction part.

# the cycle of the repeating decimal of a fraction with a prime denominator 
# is equal to the lowest number k for which 10^k mod denominator = 1

# Good number theory solution, runs in 100ms
# Down to 23.8ms when working from the top and stopping with a reptend
# of d - 1

from math import sqrt

limit = 1000
limit_root = int(sqrt(limit))
is_prime = [False, False]
is_prime += [True for n in range(2, limit_root + 1)]
for p in range(2, limit_root + 1):
    if is_prime[p]:
        c = p * p
        while c <= limit_root:
            is_prime[c] = False
            c += p
            
def check_prime(n):
    if n < limit_root: return is_prime[n]
    n_root = int(sqrt(n))
    for f in filter(lambda i: is_prime[i], range(2, n_root + 1)):
        if n % f == 0:
            return False
    return True

longest = 0
longest_d = -1

for d in range(limit, 6, -1):
    if check_prime(d):
        k = 1
        while (10 ** k) % d != 1:
            k += 1
        if k > longest: 
            longest = k
            longest_d = d
    if longest == d - 1: break