#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:22:26 2018

@author: toddbilsborough
"""

# Brute force with combinatorics, wanted to try it but it's slow as fuck
# 3.71 s

from itertools import permutations

pandigital_identities = set()
for permutation in (list(x) for x in permutations(list(range(1,10)))):
    m1 = permutation[0]
    m2 = int(''.join(map(str, permutation[1:5])))
    p = int(''.join(map(str, permutation[5:])))
    if m1 * m2 == p: pandigital_identities.add(p)
    m1 = int(''.join(map(str, permutation[0:2])))
    m2 = int(''.join(map(str, permutation[2:5])))
    p = int(''.join(map(str, permutation[5:])))
    if m1 * m2 == p: pandigital_identities.add(p)

s = sum(pandigital_identities)