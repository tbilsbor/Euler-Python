#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:25:14 2018

@author: toddbilsborough
"""

#Considering quadratics of the form:
#n2+an+b, where |a|<1000 and |b|≤1000
#where |n| is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#Find the product of the coefficients, a and b, 
# for the quadratic expression that produces the maximum number of primes 
# for consecutive values of n, starting with n=0.

# b has to be prime and a has to be odd.

# About 1 second, not great
# Down to 669ms with some optimization from the forum

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
    if n < limit_root: return is_prime[n]
    n_root = int(sqrt(n))
    for f in filter(lambda i: is_prime[i], range(2, n_root + 1)):
        if n % f == 0:
            return False
    return True

def quadratic(a, b, n):
    return (n ** 2) + (a * n) + b
        
longest = -1
product = 0
    
for b in [x for x in range(-1000, 1000) if check_prime(abs(x))]:
    step = 2
    if (1 - b) % 2 == 0: step = 1
    if (1 - b) < -999:
        start = -999
        step = 2
    else: 
        start = 1 - b
    for a in range(1 - b, 999, step):
        if step == 1: step - 2
        n = 0
        while check_prime(quadratic(a, b, n)): n += 1
        if n > longest:
            longest = n
            product = a * b