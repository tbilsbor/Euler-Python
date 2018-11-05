#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:05:32 2018

@author: toddbilsborough
"""

# Recursive from analysis file with memoization... 25.4 ms

values = [1, 2, 5, 10, 20, 50, 100, 200]
pence_to_count = 200
memo = [[0 for x in range(0, 8)] for y in range(0, pence_to_count + 1)]

def count_combos(pence, largest):
    if largest == 0: return 1
    combos = 0
    p_copy = pence
    if memo[pence][largest] > 0: return memo[pence][largest]
    while pence >= 0:
        combos += count_combos(pence, largest - 1)
        pence -= values[largest]
    memo[p_copy][largest] = combos
    return combos

combos = count_combos(pence_to_count, 7)