#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:11:38 2018

@author: toddbilsborough
"""

from math import floor, sqrt
from decimal import getcontext, Decimal

upper_bound = 10001
integers_to_capture = 500
getcontext().prec = integers_to_capture + 10
cycles = {}
for n in [x for x in range(2, upper_bound) if 
          x not in 
          [y ** 2 for y in range(2, floor(sqrt(upper_bound)) + 1)]]:
    integers = []
    root = Decimal(n).sqrt()
    for _ in range(integers_to_capture):
        integer = floor(root)
        integers.append(integer)
        root -= integer
        root = 1 / root
    cycles[n] = integers[1:]
    
odd_cycles = {}
no_cycles = {}
for n, digits in cycles.items():
    found = False
    if all([x == digits[0] for x in digits[0:11]]):
        odd_cycles[n] = (1, digits)
        found = True
        continue
    for cycle_length in range(2, integers_to_capture):
        cycle = digits[:cycle_length]
        if all([x == cycle[0] for x in cycle]): continue
        compare = digits[cycle_length: 2 * cycle_length]
        if cycle == compare:
            if cycle_length % 2 == 1:
                odd_cycles[n] = (cycle_length, digits)
                found = True
                break
            else:
                found = True
                break
    if not found:
        no_cycles[n] = digits