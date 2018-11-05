#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:45:12 2018

@author: toddbilsborough
"""

# 16.9 seconds

cubes = {}
permutations = 0
n = 1
smallest = -1
while permutations != 5:
    c = n ** 3
    cubes[c] = []
    c_copy = c
    while c_copy > 0:
        cubes[c].append(c_copy % 10)
        c_copy //= 10
    cubes[c] = sorted(cubes[c])
    permutations = 0
    for cube, perm in cubes.items():
        if len(perm) != len(cubes[c]): continue
        if perm == cubes[c]: 
            permutations += 1
            if permutations == 1: smallest = cube
    n += 1