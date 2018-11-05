#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:11:07 2018

@author: toddbilsborough
"""

from math import sqrt

#prime_set = [3, 7, 109, 673]
limit = 10000000000
limit_root = int(sqrt(limit))
is_prime = [False, False]
is_prime += [True for n in range(2, limit_root + 1)]

for p in range(2, limit_root + 1):
    if is_prime[p]:
        c = p * p
        while c <= limit_root:
            is_prime[c] = False
            c += p

#%%

def check_prime(n):
    n_root = int(sqrt(n))
    for f in range(2, n_root + 1):
        if not is_prime[f]: continue
        if n % f == 0:
            return False
    return True

def fifth_element(n):
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

#%%

s = -1
prime_set = [13]

#%%
for p in range(prime_set[-1] + 1, limit):
    if p <= limit_root and not is_prime[p]: continue
    if p > limit_root and not check_prime(p): continue
    if fifth_element(p):
        prime_set.append(p)
        s = sum(prime_set)
        break
    
#%%
        
last_element_len = len(str(prime_set[-1]))
last_element_mag = 10 ** last_element_len
low = prime_set[-1] + (prime_set[-1] * last_element_mag) + last_element_mag
for p in range(low, limit, last_element_mag):
    if p <= limit_root and not is_prime[p]: continue
    if p > limit_root and not check_prime(p): continue
    if p % last_element_mag == prime_set[-1]:
        p_copy = p
        p_copy //= last_element_mag
        if p_copy <= limit_root and is_prime[p_copy]: 
            if fifth_element(p_copy): break
        if p_copy > limit_root and check_prime(p_copy): 
            if fifth_element(p_copy): break
        if len(str(p_copy)) > last_element_len + 2: break

#%%
        
candidates = []
for p in range(37783728, limit):
    if p <= limit_root and not is_prime[p]: continue
    if p > limit_root and not check_prime(p): continue
    p_copy = p
    if p_copy % 10000 == 3727:
        c_copy = c
        c_copy //= 10000
        if is_prime[c_copy]: 
            c_copy //= 10000
            c_copy += 3727 * (10 ** len(str(c_copy)))
            if c_copy <= limit_root and is_prime[c_copy]: candidates.append(c)
            if c_copy > limit_root and check_prime(p): candidates.append(c)
        break
    
#%%
    
candidates = []
for c in candidates_two:
    c_copy = c
    c_copy //= 10000
    c_copy += 3727 * (10 ** len(str(c_copy)))
    if c_copy <= limit_root and is_prime[c_copy]: candidates.append(c)
    if c_copy > limit_root and check_prime(p): candidates.append(c)
    
#%%

candidates_two = []
for c in candidates:
    c_copy = c
    c_copy //= 100
    c_copy += 97
    if c_copy <= limit_root and is_prime[c_copy]: candidates_two.append(c)
    if c_copy > limit_root and check_prime(p): candidates_two.append(c)

#%%

candidates = []    
for c in candidates_two:
    c_copy //= 1000
    c_copy += 109 * (10 ** len(str(c_copy)))
    if c_copy <= limit_root and is_prime[c_copy]: candidates.append(c)
    if c_copy > limit_root and check_prime(p): candidates.append(c)
    
#%%
    
for c in candidates:
    c_copy = c
    c_copy //= 1000
    c_copy += 3
    if c_copy <= limit_root and not is_prime[c_copy]: candidates.remove(c)
    if c_copy > limit_root and not check_prime(p): candidates.remove(c)
    
for c in candidates:
    c_copy //= 10
    c_copy += 3 * (10 ** len(str(c_copy)))
    if c_copy <= limit_root and not is_prime[c_copy]: candidates.remove(c)
    if c_copy > limit_root and not check_prime(p): candidates.remove(c)
    
for c in candidates:
    c_copy = c
    c_copy //= 10
    c_copy += 7
    if c_copy <= limit_root and not is_prime[c_copy]: candidates.remove(c)
    if c_copy > limit_root and not check_prime(p): candidates.remove(c)
    
for c in candidates:
    c_copy //= 10
    c_copy += 7 * (10 ** len(str(c_copy)))
    if c_copy <= limit_root and not is_prime[c_copy]: candidates.remove(c)
    if c_copy > limit_root and not check_prime(p): candidates.remove(c)