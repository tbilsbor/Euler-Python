#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:39:48 2018

@author: toddbilsborough
"""

s = 0
for n in range(2, 354295):
    n_copy = n
    sum_of_fifth_powers = 0
    while n_copy > 0:
        digit = n_copy % 10
        sum_of_fifth_powers += digit ** 5
        n_copy //= 10
    if sum_of_fifth_powers == n:
        s += n