# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# How many routes are there through a 20×20 grid?

# My hypothesis is that it's going to be the middle number
# of the 2n - 1th row of Pascal's Triangle

# My hypothesis is correct, runs in 12.4 ms

grid_size = 20
pascal = []
pascal.append([1])

for r in range(1, (2 * grid_size) + 1):
    pascal.append([])
    for c in range(0, r + 1):
        if c == 0:
            pascal[r].append(1)
        elif c == r:
            pascal[r].append(1)
        else:
            next_pascal = pascal[r - 1][c - 1] + pascal[r - 1][c]
            pascal[r].append(next_pascal)
            
paths = pascal[grid_size * 2][grid_size]