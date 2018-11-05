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
# v2, further refinement using formula for triangle numbers
# n * (n + 1) / 2
# Actually puts it at 1.35 seconds, so that's a little worse

primes = [2]
p = 3
# Upper bound guess based on sqrt of largest 32-bit int
while p <= 46340: 
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

n = 1
factors = 0
while factors <= 500:
    n += 1
    n1 = n + 1
    if n % 2 == 0:
        factors = get_factors(n/2) * get_factors(n1)
    else: 
        factors = get_factors(n) * get_factors(n1/2)
    
#print(int((n * (n + 1))/2))