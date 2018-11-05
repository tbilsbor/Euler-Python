#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:45 2018

@author: toddbilsborough
"""

# Optimization - don't get the sums of all the abundant numbers
# For each number under the limit, subtract all the abundant numbers
# If the resulting number is in the abundant numbers, then it's not
# added to the running total
# Stupidly slow

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

limit = 28124

abundant = list(n for n in range(12, limit - 12) if 
                sum_of_proper_divisors(n) > n)

s = 0
for n in range(0, limit):
    i = 0
    not_sum = True
    while abundant[i] < n:
        diff = n - abundant[i]
        if diff in abundant:
            not_sum = False
            break
        i += 1
    if not_sum:
        s += n