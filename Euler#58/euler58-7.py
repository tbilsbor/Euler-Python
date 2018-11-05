#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:42:54 2018

@author: toddbilsborough
"""

ratio = 1
spiral_ur = [1]
spiral_ul = [1]
spiral_ll = [1]
n = 1
primes_count = 0
is_prime = [False, False, True]
low = 3

# Only checking to the square root of the upper bound?
# Having two arrays: one is the base prime list, up to the square root
# of the upper bound
# The second is the segment you're checking
# so you'll have to expand the base list every time
# you might have to sub-chunk the primes if the intervals get big enough
# Maybe don't do the primes in the middle of the function but
# generate the spiral first out to a certain limit and then get the primes
# up to that limit

while ratio > 0.3:
    spiral_ul.append((4 * (n ** 2)) + 1)
    n += 1
    spiral_ur.append((4 * (n ** 2)) - (10 * n) + 7)
    spiral_ll.append((4 * (n ** 2)) - (6 * n) + 3)
    
    high = spiral_ll[-1]
    is_prime += [True for n in range(low, high + 1)]
    for i in range(2, low):
        if not is_prime[i]:
            continue
        c = i * (low // i)
        if c == i: c += i
        while c < high:
            is_prime[c] = False
            c += i
    low = high
    
    if is_prime[spiral_ur[-1]]: primes_count += 1
    if is_prime[spiral_ul[-1]]: primes_count += 1
    if is_prime[spiral_ll[-1]]: primes_count += 1
    ratio = primes_count / ((4 * (n - 1)) + 1)
        
    side_length = n * 2 - 1