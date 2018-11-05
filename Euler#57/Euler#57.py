#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:52:45 2018

@author: toddbilsborough
"""

# 141 ms

numerators = [3, 7]
denominators = [2, 5]
limit = 1000
next_numerator = lambda n: 2 * numerators[n - 1] + numerators[n - 2]
next_denominator = lambda n: 2 * denominators[n - 1] + denominators[n - 2]

def digits_count(n):
    d = 0
    while n > 0:
        n //= 10
        d += 1
    return d

s = 0
for n in range(2, limit):
    numerators.append(next_numerator(n))
    denominators.append(next_denominator(n))
    if digits_count(numerators[-1]) > digits_count(denominators[-1]):
        s += 1