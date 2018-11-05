#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:55:51 2018

@author: toddbilsborough

"""
from math import sqrt

limit = 1000000000
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
    n_root = int(sqrt(n))
    for f in range(2, n_root + 1):
        if not is_prime[f]: continue
        if n % f == 0:
            return False
    return True
            
ratio = 1
n = 1
next_ul = lambda n: (4 * (n ** 2)) + 1
next_ur = lambda n: (4 * (n ** 2)) - (10 * n) + 7
next_ll = lambda n: (4 * (n ** 2)) - (6 * n) + 3
primes_count = 0

while ratio > 0.1:
    next_num = next_ul(n)
    if check_prime(next_num): primes_count += 1        
    n += 1    
    next_num = next_ur(n)
    if check_prime(next_num): primes_count += 1
    next_num = next_ll(n)
    if check_prime(next_num): primes_count += 1    
    ratio = primes_count / ((4 * (n - 1)) + 1)
    
side_length = n * 2 - 1