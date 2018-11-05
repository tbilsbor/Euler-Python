#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:41:36 2018

@author: toddbilsborough
"""

from math import sqrt

limit = 500000000
is_prime = [True for n in range(limit + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(int(sqrt(limit))):
    if not is_prime[i]:
        continue
    c = i * i
    while c <= limit:
        is_prime[c] = False
        c += i
        
# Not calculating the lower right diagonal because those are all odd squares        

n = 1
spiral_ur = [1]
spiral_ul = [1]
spiral_ll = [1]
ratio = 1
primes_count = 0
while n < limit:
    spiral_ul.append((4 * (n ** 2)) + 1)
    n += 1
    spiral_ur.append((4 * (n ** 2)) - (10 * n) + 7)
    spiral_ll.append((4 * (n ** 2)) - (6 * n) + 3)
    if is_prime[spiral_ur[-1]]: primes_count += 1
    if is_prime[spiral_ul[-1]]: primes_count += 1
    if is_prime[spiral_ll[-1]]: primes_count += 1
    ratio = primes_count / ((4 * (n - 1)) + 1)
    
side_length = n * 2 - 1