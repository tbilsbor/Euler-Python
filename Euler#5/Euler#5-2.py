#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:33:10 2018

@author: toddbilsborough
"""

# Variation on #5: Find the smallest number evenly divisible
# By all the numbers from 1 to k

# 12.9 ms even for k = 300

k = 300
primes = [2]
p = 3
s = 1
while p <= k:
    i = 0
    isPrime = True
    while primes[i] * primes[i] <= p:
        if p % primes[i] == 0:
            isPrime = False
            break
        i += 1
    if isPrime:
        primes.append(p)
    p += 2

for i in range(0, len(primes)):
    e = 1
    while primes[i] ** e <= k:
        s *= primes[i]
        e += 1
    
#print(s)