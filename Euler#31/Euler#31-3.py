#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:05:32 2018

@author: toddbilsborough
"""

# Dynamic programming solution I don't entirely underestand
# 25.2

values = [1, 2, 5, 10, 20, 50, 100, 200]
pence_to_count = 200
combos = [0 for x in range(201)]
combos[0] = 1
for i in range(8):
    for j in range(values[i], pence_to_count + 1):
        combos[j] += combos[j - values[i]]
c = combos[pence_to_count]