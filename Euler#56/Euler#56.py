#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:05:08 2018

@author: toddbilsborough
"""

# Considering natural numbers of the form, ab, where a, b < 100, 
# what is the maximum digital sum?
# Runs in 298 ms

def get_digital_sum(n):
    d_sum = 0
    while n > 0:
        d_sum += n % 10
        n //= 10
    return d_sum

largest = -1
for n in [a ** b for a in range(99, 0, -1) for b in range(99, 2, -1)]:
    digital_sum = get_digital_sum(n)
    if digital_sum > largest:
        largest = digital_sum
        
print(largest)