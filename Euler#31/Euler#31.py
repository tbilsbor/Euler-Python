#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:05:32 2018

@author: toddbilsborough
"""

# Recursive solution, runs in 25.9 ms

values = [1, 2, 5, 10, 20, 50, 100, 200]

def count_combos(pence, coin):
    if coin == 1:
        return 1
    elif coin == 2:
        return pence // 2
    else:
        combos = 0
        for sub_coin in [x for x in values if x < coin]:
            p_copy = pence - coin
            while p_copy >= 0:
                combos += count_combos(p_copy, sub_coin)
                p_copy -= coin
        return combos

pence_to_count = 200
combos = 0
for coin in [x for x in values if x <= pence_to_count]:
    combos += count_combos(pence_to_count, coin)