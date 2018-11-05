#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:45 2018

@author: toddbilsborough
"""

# From the analysis file
# First iteration, 123ms, about the same as my initial solution

from math import sqrt

def sum_of_proper_divisors(n):
    if n == 1: return 0
    r = int(sqrt(n))
    if r ** 2 == n:
        s = 1 + r
        r -= 1
    else:
        s = 1
    if n % 2 == 0:
        f = 2
        step = 1
    else:
        f = 3
        step = 2
    while f <= r:
        if n % f == 0: s += f + (n // f)
        f += step
    return s

s = 0
for a in range(2, 9999):
    b = sum_of_proper_divisors(a)
    if b > a:
        if sum_of_proper_divisors(b) == a:
            s += a + b