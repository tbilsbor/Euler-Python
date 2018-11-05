#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:37:53 2018

@author: toddbilsborough
"""

# What is the value of the first triangle number 
# to have over five hundred divisors?

# Formula based solution based on prime factor exponents
# 6.03 s
# Added prime bootstrapper and checking only divisibility by primes
# 1.31 s

primes = [2]
p = 3
while p <= 46340: # Upper bound guess based on sqrt of largest 32-bit int
    i = 0
    is_prime = True
    while primes[i] ** 2 <= p:
        if p % primes[i] == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(p)
    p += 2

def get_factors(n):
    nCopy = n
    i = 0
    exp_product = 1
    while nCopy > 1:
        exp_count = 1
        while nCopy % primes[i] == 0:
            exp_count += 1
            nCopy /= primes[i]
        i += 1
        exp_product *= exp_count
    return exp_product

next_triangle = 1
n = 1
factors = 0
while factors <= 500:
    n += 1
    next_triangle += n
    factors = get_factors(next_triangle)
    
#print(next_triangle)