#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:34:49 2018

@author: toddbilsborough
"""

# Which starting number, under one million, 
# produces the longest Collatz chain?
# Naive solution takes a long time to run, maybe over a minute
# Avoiding re-calculation brings it down to 3.54 s

longest = -1
longest_count = -1
collatz = {}
for n in range(2, 1000000):
    count = 1
    n_copy = n
    while n_copy > 1:
        if n_copy in collatz:
            count += collatz[n_copy]
            break
        if n_copy % 2 == 0:
            n_copy //= 2
        else: n_copy = (n_copy * 3) + 1
        count += 1
    collatz[n] = count
    if count > longest_count:
        longest_count = count
        longest = n
        
#print(longest)