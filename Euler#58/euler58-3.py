#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:41:36 2018

@author: toddbilsborough
"""

# Bootstrapper
# Primes to...
# 1000: 13.6ms
# 10000: 31.5ms
# 100000: 321ms
# 200000: 760ms

limit = 200000
primes = [2, 3, 5, 7]
p = 11
step = 4
while p < limit:
    is_prime = True
    i = 0
    while primes[i] * primes[i] <= p:
        if p % primes[i] == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(p)
    if step == 4:
        step = 2
    elif step == 2:
        step = 4
    p += step