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
# Recursion doesn't seem to work well

collatz = {1:1}

def count_chain(n):
    if n in collatz:
        return n
    if n % 2 == 0:
        collatz[n] = 1 + count_chain(n / 2)
    else:
        collatz[n] = 2 + count_chain((3 * n + 1) / 2)
    return collatz[n]

longest = -1
longest_count = -1    
for n in range(500001, 1000000):
    count = count_chain(n)
    if count > longest_count:
        longest_count = count
        longest = n
        
print(longest)
