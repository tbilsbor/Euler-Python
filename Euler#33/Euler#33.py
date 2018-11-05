#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:38:28 2018

@author: toddbilsborough
"""

# Basic optimized brute force, 29.2 ms

fractions = [(n, d)
             for n in range(11, 100) if n % 10 != 0
             for d in range(n + 1, 100) if d % 10 != 0]
product = [1, 1]

for fraction in fractions:
    decimal_value = fraction[0] / fraction[1]
    n_digits = [int(digit) for digit in str(fraction[0])]
    d_digits = [int(digit) for digit in str(fraction[1])]
    check = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for tup in check:
        n_inverse = 1 if tup[0] == 0 else 0
        d_inverse = 1 if tup[1] == 0 else 0
        if (n_digits[tup[0]] == d_digits[tup[1]] and
            n_digits[n_inverse] / d_digits[d_inverse] == decimal_value):
            product = list(map(lambda i: product[i] * fraction[i], range(2)))
            continue

if product[1] / product[0] % 1 == 0:
    product[1] = product[1] // product[0]
    product[0] = 1