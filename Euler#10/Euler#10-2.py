#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:38:44 2018

@author: toddbilsborough
"""

# Find the sum of primes below 2 million
# Sieve

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

p = 3
sum_of_primes = 2
while p < 2000000:
    if is_prime(p):
        sum_of_primes += p
    p += 2

print(sum_of_primes)