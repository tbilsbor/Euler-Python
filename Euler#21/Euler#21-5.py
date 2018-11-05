#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:45 2018

@author: toddbilsborough
"""

# From the analysis file
# Third iteration, literal copy of analysis file
# Now we're talking; down to 66.6 ms

# Basically takes the sum of divisors function and breaks it up into steps
# (prime ** (e + 1) - 1) // (prime - 1)
# j starts as p * p, and then is multiplied by p every further time it divides
# that takes care of prime ** (e + 1)
# Then the running sum is multiplied by that - 1
# and then divided by p - 1

# if n > 1: s *= (n + 1) takes care of the last prime
# but I'm not entirely clear how

def sum_of_proper_divisors(n):
    s = 1
    p = 2
    nCopy = n
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n //= p
            while n % p == 0:
                j *= p
                n //= p
            s *= (j - 1)
            s //= (p - 1)
        if p == 2: 
            p = 3 
        else: 
            p += 2
    if n > 1: 
        s *= (n + 1)
    s -= nCopy
    return s

s = 0
for a in range(2, 9999):
    b = sum_of_proper_divisors(a)
    if b > a:
        if sum_of_proper_divisors(b) == a:
            s += a + b