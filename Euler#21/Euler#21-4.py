#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:45 2018

@author: toddbilsborough
"""

# From the analysis file
# Second iteration, using prime factorization
# sigma (sum of prime factors) of p = (p ** (a + 1) - 1)/(p - 1)
# sigma of a composite number is the product of the sigma functions
# of its prime factorization
# sum of proper divisors of n is sigma function minus n

# Seems to be considerably worse, at 1.16 s even with a prime bootstrappera

from math import sqrt

primes = [2]
p = 3
while p <= 20000:
    i = 0
    is_prime = True
    while primes[i] <= int(sqrt(p)) and i < len(primes):
        if p % primes[i] == 0: 
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(p)
    p += 2

def sum_of_proper_divisors(n):
    if n in primes: return 1
    nCopy = n
    s = 1
    i = 0
    while n > 1:
        e = 0
        prime = primes[i]
        while n % prime == 0:
            e += 1
            n //= prime
        s *= (prime ** (e + 1) - 1) // (prime - 1)
        i += 1
    s -= nCopy
    return s

s = 0
for a in range(2, 9999):
    b = sum_of_proper_divisors(a)
    if b > a:
        if sum_of_proper_divisors(b) == a:
            s += a + b