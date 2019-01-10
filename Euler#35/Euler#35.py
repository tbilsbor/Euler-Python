#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:00:21 2018

@author: toddbilsborough
"""

# 13.4 sec

from math import sqrt

limit = 1000000
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

def rotate(n):
    return n[-1] + n[0:-1]

count = 0
blacklist = "245680"
for n in (n for n in range(limit + 1) if check_prime(n)):
    n_str = rotate(str(n))
    if int(n_str) == n:
        count += 1
        continue
    if any(x in n_str for x in blacklist):
        continue
    rotatable = True
    while int(n_str) != n:
        if not check_prime(int(n_str)): 
            rotatable = False
            break
        n_str = rotate(n_str)
    if rotatable: count += 1