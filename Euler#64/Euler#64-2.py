#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:11:38 2018

@author: toddbilsborough
"""

from math import floor, sqrt
from decimal import getcontext, Decimal

upper_bound = 10001 # Examine non-square integers less than this
getcontext().prec = 1000 # Precision of square root
odd_cycles = {} # Holds odd cycles indexed by the integer it's derived from
even_cycles = {}
# Check up to this value before assuming cycle length 1
minimum_length = 20
"""for non-square integers in range"""
for n in [x for x in range(2, upper_bound) if 
          x not in 
          [y ** 2 for y in range(2, floor(sqrt(upper_bound)) + 1)]]:
    integers = [] # Holds the integers of the square root as generated
    largest = -1 # Largest integer found in cycle; fast check for repeats
    root = Decimal(n).sqrt()
    found = False
    """ignore the first integer component"""
    integer = floor(root)
    root -= integer
    root = 1 / root
    """until a cycle is found"""
    while not found:
        """generate the next integer"""
        integer = floor(root)
        if integer > largest: largest = integer
        integers.append(integer)
        root -= integer
        root = 1 / root
        """look for single cycles"""
        if len(integers) < minimum_length: continue
        if all([x == integers[0] for x in integers]):
            found = True
            odd_cycles[n] = (1, integers)
            break
        """fast check for cycles"""
        if integers.count(largest) < 2: continue
        """look for longer cycles"""
        start_length = integers.index(largest) + 1
        for cycle_length in range(start_length, len(integers) // 2 + 1):
            cycle = integers[:cycle_length]
            compare = integers[cycle_length:cycle_length * 2]
            if cycle == compare:
                if cycle_length % 2 == 1:
                    odd_cycles[n] = (cycle_length, integers)
                    found = True
                    break
                else:
                    even_cycles[n] = (cycle_length, integers)
                    found = True
                    break