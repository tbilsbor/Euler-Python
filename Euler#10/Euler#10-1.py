#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:29:58 2018

@author: toddbilsborough
"""

# Find the sum of primes below 2 million
# Bootstrapper - superior even for large n

from math import sqrt

primes = [2]
p = 3
while p < 2000000:
    is_prime = True
    r = int(sqrt(p))
    i = 0
    while primes[i] <= r:
        if p % primes[i] == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(p)
    p += 2

sum_of_primes = sum(primes, 0)
print(sum_of_primes)