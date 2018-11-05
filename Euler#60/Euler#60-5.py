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
sub_limit = 10000

for p in range(2, limit_root + 1):
    if is_prime[p]:
        c = p * p
        while c <= limit_root:
            is_prime[c] = False
            c += p
            
primes = list(filter(lambda i: is_prime[i], range(2, sub_limit + 1)))

# Functions

def check_prime(n):
    if n < limit_root: return is_prime[n]
    n_root = int(sqrt(n))
    for f in list(filter(lambda i: is_prime[i], range(3, n_root + 1))):
        if n % f == 0:
            return False
    return True

def check_concatenation(n, p):
    concat = int(str(p) + str(n))
    if not check_prime(concat):
        return False
    concat = int(str(n) + str(p))
    if not check_prime(concat):
        return False
    return True

def next_element(n, p_set):
    for p in p_set:
        if not check_concatenation(n, p):
            return False
    return True

def get_elements(p_set):
    prime_set = p_set
    if len(prime_set) == 5:
        s = sum(prime_set)
        return s
    higher_primes = filter(lambda x: x > prime_set[-1], primes)
    for p in higher_primes:
        if next_element(p, prime_set):
            prime_set.append(p)
            if get_elements(prime_set) > -1:
                s = sum(prime_set)
                return s
            else:
                prime_set.remove(prime_set[-1])
                continue
    return -1

for prime in primes:
    s = get_elements([prime])
    if s > -1: break