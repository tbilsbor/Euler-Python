#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:48:32 2018

@author: toddbilsborough
"""

# Solution using Fibonacci formula for even numbers
# E(n) = 4 * E(n-1) + E(n-2)
# This version is very slightly faster

fib = [2, 8]
n = 2
total = 10
limit = 4000000

next_even = 4 * fib[n-1] + fib[n-2]
while next_even < limit:
    fib.append(next_even)
    total += next_even
    n += 1
    next_even = 4 * fib[n-1] + fib[n-2]
