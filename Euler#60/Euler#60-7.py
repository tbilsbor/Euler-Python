#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:08:23 2018

@author: toddbilsborough
"""

# From math blog

from math import sqrt
   
limit = 30000 ** 2
limit_root = 30000
is_prime = [False, False]
is_prime += [True for n in range(2, limit_root + 1)]
pairs = list([] for i in range(2, limit_root + 1))

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

def make_pairs(a):
    pair_set = []
    for b in range(a + 1, limit_root + 1):
        if check_prime(int(str(a) + str(b))) \
        and check_prime(int(str(b) + str(a))):
            pair_set.append(b)
    pairs[a] += pair_set
    
primes = list(filter(lambda i: is_prime[i], range(2, limit_root + 1)))
s = 30000 * 5

for i in range(0, len(primes)):
    p = primes[i]
    if p * 5 > s: break
    if len(pairs[p]) == 0: make_pairs(p)
    for j in range(0, len(pairs[p])):
        p2 = pairs[p][j]
        if p + p2 * 4 > s: break
        if len(pairs[p2]) == 0: make_pairs(p2)
        j_set = set(pairs[p2])
        test_set = [x for x in pairs[i] if x in j_set]
        if len(test_set) == 0: continue
        for k in range(0, len(test_set)):
            p3 = pairs[j][k]
            if p + p2 + p3 * 3 > s: break
            if len(pairs[p3]) == 0: make_pairs(p3)
            k_set = set(pairs[k])
            test_set = [x for x in test_set if x in k_set]
            if len(test_set) == 0: continue        
            for l in range(0, len(test_set)):
                p4 = pairs[k][l]
                if p + p2 + p3 + p4 * 2 > s: break
                if len(pairs[p3]) == 0: make_pairs(p3)
                l_set = set(pairs[l])
                test_set = [x for x in test_set if x in l_set]
                if len(test_set) == 0: continue
                m = min(test_set)
                if p + p2 + p3 + p4 + m < s:
                    s = primes[i] + primes[j] + primes[k] + primes[l] + m