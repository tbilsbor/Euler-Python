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
    n_root = int(sqrt(n))
    for f in list(filter(lambda i: is_prime[i], range(2, n_root + 1))):
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

# Program

prime_set = [3]
primes_offset = 3     
sub_limit = 250000     
while len(prime_set) < 5:
    last_element_len = len(str(prime_set[-1]))
    last_element_mag = 10 ** last_element_len
    low = prime_set[-1] + (prime_set[-1] * last_element_mag) + last_element_mag
    for p in range(low, limit, last_element_mag):
        p_copy = p
        p_copy //= last_element_mag
        if p_copy <= limit_root and is_prime[p_copy]: 
            if next_element(p_copy): 
                prime_set.append(p_copy)
                print(prime_set)
                break
        if p_copy > limit_root and check_prime(p_copy): 
            if next_element(p_copy): 
                prime_set.append(p_copy)
                print(prime_set)
                break
        if p_copy > sub_limit:
            if next_start_prime(primes_offset) == 5:
                primes_offset += 1
            prime_set = []
            prime_set.append(next_start_prime(primes_offset))
            print(prime_set)
            primes_offset += 1
            break
            
s = sum(prime_set)