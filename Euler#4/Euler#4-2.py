#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:52:42 2018

@author: toddbilsborough
"""

# Improved solution
# a > b, so that eliminates about half, brings it down to 1.52 s from 2.97 s

# Starts from the top to find the largest faster, but doesn't find the
# largest first
# stop checking a and b that would
# be too small to improve upon the largest palindrome found so far.
# (see the documentation; further improvements follow)

largest = -1
for product in [a * b 
                for a in range(999, 100, - 1) 
                for b in range(a, 100, -1)]:
    p = product
    digits = []
    match = True
    while p > 0:
        digit = p % 10
        digits.append(digit)
        p //= 10
    length = len(digits) // 2
    for d in range(0, length):
        if digits[d] != digits[-d - 1]:
            match = False
            break
    if match and product > largest:
        largest = product
        break
        
print (largest)