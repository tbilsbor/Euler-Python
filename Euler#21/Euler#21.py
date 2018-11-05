#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:14:06 2018

@author: toddbilsborough
"""

# Naive solution, pure brute force, 122 ms

from math import sqrt

sums = [0, 0]
amicable_sum = 0
for n in range(2, 10000):
    sum_of_divisors = 0
    for d in range(1, int(sqrt(n))):
        if n % d == 0:
            sum_of_divisors += d
            if d > 1: sum_of_divisors += n // d
    sums.append(sum_of_divisors)
    if sum_of_divisors < n:
        if sums[sum_of_divisors] == n:
            amicable_sum += sum_of_divisors
            amicable_sum += sums[sum_of_divisors]