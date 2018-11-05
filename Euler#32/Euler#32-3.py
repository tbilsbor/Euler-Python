#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:22:26 2018

@author: toddbilsborough
"""

pangit = [str(x) for x in range(1,10)]
luppi = []

for x in range(0,10000):
    for y in range(0,10000):
        if sorted(str(x)+str(y)+str(x*y)) == pangit:
            luppi.append(int(x*y))

print(sum(set(luppi)))