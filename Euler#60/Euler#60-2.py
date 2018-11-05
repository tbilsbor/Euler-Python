#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:11:07 2018

@author: toddbilsborough
"""

from math import sqrt

limit = 10000000
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

def next_element(n):
    for p in prime_set:
        concat = int(str(p) + str(n))
        if concat > limit_root:
            if not check_prime(concat):
                return False
        else:
            if not is_prime[concat]:
                return False
        concat = int(str(n) + str(p))
        if concat > limit_root:
            if not check_prime(concat):
                return False
        else:
            if not is_prime[concat]:
                return False
    return True

def next_start_prime(offset):
    count = 0
    for i in range(0, limit_root):
        if is_prime[i]:
            count += 1
            if count == offset: return i

prime_set = [3]
prime_offset = 2
candidate_sets = []
while len(prime_set) < 5:
    for p in range(prime_set[-1] + 1, limit):
        if p <= limit_root and not is_prime[p]: continue
        if p > limit_root and not check_prime(p): continue
        concat = int(str(p) + str(prime_set[-1]))
        if concat > limit:
            prime_set = []
            prime_offset += 1
            prime_set.append(next_start_prime(prime_offset))
            break
        if next_element(p):
            prime_set.append(p)
            if len(prime_set) == 4:
                candidate_sets.append(prime_set)
                prime_set = []
                prime_offset += 1
                prime_set.append(next_start_prime(prime_offset))
            break
    
s = sum(prime_set)