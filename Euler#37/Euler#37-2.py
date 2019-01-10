#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:40:07 2018

@author: toddbilsborough
"""

# 12.5 seconds 
# down to 12 seconds by removing the string conversions

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

found = 0
s = 0
blacklist = "245680"
for n in (x for x in range(11, limit) if check_prime(x)):
    match = True
    if any(d in str(n) for d in blacklist): continue
    trunc_right = n
    trunc_left = n
    trunc_factor = len(str(trunc_right)) - 1
    while trunc_right > 9:
        trunc_right = trunc_right % 10 ** trunc_factor
        trunc_left = trunc_left // 10
        if (not check_prime(trunc_right) or
            not check_prime(trunc_left)):
            match = False
            break
        trunc_factor -= 1
    if not match: continue
    found += 1
    s += n
    if found == 11: break