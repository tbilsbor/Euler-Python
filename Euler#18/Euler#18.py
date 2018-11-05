#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:13:32 2018

@author: toddbilsborough
"""

# 13.2 ms, not bad from an algorithmic standpoint, could be more pythonic

triangle_string = ("75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 "
                   "19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 "
                   "04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 "
                   "41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 "
                   "43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 "
                   "68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 "
                   "48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 "
                   "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

triangle = []
results = []
row_count = 0
capture_start = 0
for r in range(0, 15):
    triangle.append([])
    results.append([])
    row_count += 1
    for c in range(0, row_count):
        num = int(triangle_string[capture_start]) * 10
        num += int(triangle_string[capture_start + 1])
        triangle[r].append(num)
        results[r].append(-1)
        capture_start += 3

results[0][0] = 75        
for r in range(1, 15):
    for c in range(0, len(triangle[r])):
        if c == 0:
            results[r][c] = results[r - 1][0] + triangle[r][c]
        elif c == len(triangle[r]) - 1:
            results[r][c] = results[r - 1][c - 1] + triangle[r][c]
        else:
            results[r][c] = max(results[r - 1][c - 1], 
                   results[r - 1][c]) + triangle[r][c]

largest = max(results[14])