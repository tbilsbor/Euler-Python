#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:41:36 2018

@author: toddbilsborough
"""

limit = 200000
is_prime = [True for n in range(limit)]
is_prime[0] = False
for i in range(1, limit):
    j = i
    while i + j + (2 * i * j) < limit:
        is_prime[i + j + (2 * i * j)] = False
        j += 1
primes = [2]
for i in range(limit):
    if is_prime[i]:
        primes.append(2 * i + 1)