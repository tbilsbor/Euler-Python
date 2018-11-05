#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:45 2018

@author: toddbilsborough
"""

# Fairly naive solution with good divisors function
# Miserable performance at 6.1s
# Removing duplicates from the summation results in mild improvement, 4.84s
# Similar algorithm in C# is 1.7s

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

abundant = list(n for n in range(12, 28124 - 12) if 
                sum_of_proper_divisors(n) > n)

sums = set(a + b for a in abundant for 
           b in abundant if 
           b >= a)

s = sum(list(n for n in range(1, 28124) if n not in sums))