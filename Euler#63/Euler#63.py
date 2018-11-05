#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:15:53 2018

@author: toddbilsborough
"""

# Brute force with good upper bounds, 13.5 ms

cnt = 0

for e in range(1, 22):
    for n in range(1, 10):
        p = n ** e
        if len(str(p)) == e: cnt += 1