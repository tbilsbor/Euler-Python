#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:45:12 2018

@author: toddbilsborough
"""

# Solution from the formums, down to 60.4ms
# Keeps track as it goes, no re-iterating over all the cubes

permutations = {}
n = 1
first = -1

while True:
    cube = str(sorted(list(str(n ** 3))))
    if cube in permutations: 
        permutations[cube]["count"] += 1
    else:
        permutations[cube] = {"count": 1, "first_cube": n ** 3}
    if permutations[cube]["count"] == 5:
        first = permutations[cube]["first_cube"]
        break
    n += 1
    