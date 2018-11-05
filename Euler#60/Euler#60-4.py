#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:48:13 2018

@author: toddbilsborough
"""

from math import sqrt

# Initial prime generation

limit = 1000000000000
limit_root = int(sqrt(limit))
is_prime = [False, False]
is_prime += [True for n in range(2, limit_root + 1)]

prime_set = []

for p in range(2, limit_root + 1):
    if is_prime[p]:
        c = p * p
        while c <= limit_root:
            is_prime[c] = False
            c += p

# Functions

def check_prime(n):
    if n < limit_root: return is_prime[n]
    n_root = int(sqrt(n))
    for f in list(filter(lambda i: is_prime[i], range(3, n_root + 1))):
        if n % f == 0:
            return False
    return True

def next_element(n):
    if not check_prime(n): return False
    for p in prime_set:
        concat = int(str(p) + str(n))
        if not check_prime(concat):
            return False
        concat = int(str(n) + str(p))
        if not check_prime(concat):
            return False
    return True

def next_start_prime(offset):
    return list(filter(lambda i: is_prime[i], 
                       range(2, limit_root + 1)))[offset]

#%%

# Program
            
prime_set = [3]
candidates = []
primes_offset = 3   
sub_limit = 100000
s = 3
while len(prime_set) < 5:
    p = prime_set[-1] + 2
    while not next_element(p) and s < sub_limit:
        p += 2
        s = sum(prime_set) + p
    if s >= sub_limit:
        if next_start_prime(primes_offset) == 5:
            primes_offset += 1
        prime_set = []
        prime_set.append(next_start_prime(primes_offset))
        s = sum(prime_set)
        primes_offset += 1
        continue
    prime_set.append(p)
    if len(prime_set) >= 4:
        print(prime_set)
        candidates.append(prime_set)
    if p > sub_limit:
        break
    
s = sum(prime_set)

#%%

sub_limit = 500000
for prime_set in candidates:
    print(prime_set)
    p = prime_set[-1] + 2
    s = sum(prime_set)
    while not next_element(p) and s < sub_limit:
        p += 2
        s = sum(prime_set) + p
    if s >= sub_limit:
        continue
    if next_element(p): break

s = sum(prime_set) + p

#%%

prime_set = [3]
candidates = []
primes_offset = 3   
sub_limit = 100000
s = 3
while len(prime_set) < 5:
    p = prime_set[-1] + 2
    while not next_element(p) and s < sub_limit:
        p += 2
        s = sum(prime_set) + p
    if s >= sub_limit:
        if next_start_prime(primes_offset) == 5:
            primes_offset += 1
        prime_set = []
        prime_set.append(next_start_prime(primes_offset))
        s = sum(prime_set)
        primes_offset += 1
        continue
    prime_set.append(p)
    if len(prime_set) >= 4:
        print(prime_set)
        candidates.append(prime_set)
    if p > sub_limit:
        break
    
s = sum(prime_set)