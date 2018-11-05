#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:35:46 2018

@author: toddbilsborough
"""

n = 1
ur = [1]
ul = [1]
ll = [1]
lr = [1]
primes = [2]

def expand_primes(n):
    if primes[-1] == 2:
        start = 3
    else:
        start = primes[-1] + 2
    for p in range(start, n + 1):
        is_prime = True
        i = 0
        while primes[i] * primes[i] <= p:
            if p % primes[i] == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(p)

ratio = 1
primes_count = 0
while ratio > 0.1:
    ul.append((4 * (n ** 2)) + 1)
    lr.append(((2 * n) + 1) ** 2)
    n += 1
    ur.append((4 * (n ** 2)) - (10 * n) + 7)
    ll.append((4 * (n ** 2)) - (6 * n) + 3)
    expand_primes(lr[-1])
    if ur[-1] in primes: primes_count += 1
    if ul[-1] in primes: primes_count += 1
    if ll[-1] in primes: primes_count += 1
    if lr[-1] in primes: primes_count += 1
    ratio = primes_count / ((4 * (n - 1)) + 1)
    
side_length = n * 2 - 1