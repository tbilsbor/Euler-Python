#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:41:36 2018

@author: toddbilsborough
"""

from math import sqrt

# Segmented sieve of Eratosthenes

limit = 1000000

is_prime = [True for n in range(limit + 1)]
is_prime[0] = False
is_prime[1] = False
low = 0
high = int(sqrt(limit)) + 1
for i in range(high):
    if not is_prime[i]:
        continue
    c = i * i
    while c <= high:
        is_prime[c] = False
        c += i
segment_size = int(sqrt(limit))
low = high
segment = 2
while segment <= int(sqrt(limit)):
    high = segment_size * segment
    for i in range(0, low):
        if is_prime[i]:
            c = i * (low // i)
            while c <= high:
                is_prime[c] = False
                c += i
    low = high
    segment += 1
high = limit
for i in range(0, low):
    if is_prime[i]:
        c = i * (low // i)
        while c <= high:
            is_prime[c] = False
            c += i
  
# Not calculating the lower right diagonal because those are all odd squares        

#n = 1
#spiral_ur = [1]
#spiral_ul = [1]
#spiral_ll = [1]
#ratio = 1
#primes_count = 0
#while n < limit:
#    spiral_ul.append((4 * (n ** 2)) + 1)
#    n += 1
#    spiral_ur.append((4 * (n ** 2)) - (10 * n) + 7)
#    spiral_ll.append((4 * (n ** 2)) - (6 * n) + 3)
#    if is_prime[spiral_ur[-1]]: primes_count += 1
#    if is_prime[spiral_ul[-1]]: primes_count += 1
#    if is_prime[spiral_ll[-1]]: primes_count += 1
#    ratio = primes_count / ((4 * (n - 1)) + 1)
#    
#side_length = n * 2 - 1