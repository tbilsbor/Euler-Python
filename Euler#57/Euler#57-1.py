#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:52:45 2018

@author: toddbilsborough
"""

# Variation using len(str) instead of modular digit chopping
# Down to 17.1ms
# Very slight improvement (16.9ms) when calculating the numerator
# based on the denominator

numerators = [3, 7]
denominators = [2, 5]
limit = 1000
next_denominator = lambda n: 2 * denominators[n - 1] + denominators[n - 2]
next_numerator = lambda n: denominators[n] + denominators[n - 1]

s = 0
for n in range(2, limit):
    denominators.append(next_denominator(n))
    numerators.append(next_numerator(n))
    if len(str(numerators[-1])) > len(str(denominators[-1])):
        s += 1