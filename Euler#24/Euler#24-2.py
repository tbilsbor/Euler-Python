#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:14:09 2018

@author: toddbilsborough
"""

# Direct calculation, as with the C# implementation
# 13 ms

from math import factorial

permutation = []
permutation_to_find = 1000000
digits = 10
s = 0

for position in range(0, 10):
    for digit in range(0, 10):
        if digit in permutation: 
            continue
        if digits - position - 1 > 0:
            factorial_value = factorial(digits - position - 1)
            if s + factorial_value >= permutation_to_find:
                permutation.append(digit)
                break
            else:
                s += factorial_value
                continue
        else:
            permutation.append(digit)
            break