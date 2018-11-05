#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:22:26 2018

@author: toddbilsborough
"""

# Multiply then check for pandigital
# Even slower, 27.7 s

pandigital = [str(x) for x in range(1, 10)]
pandigital_products = set()

for x in range(1, 1000):
    for y in range(100, 10000):
        if sorted(str(x) + str(y) + str(x * y)) == pandigital:
            pandigital_products.add(int(x * y))

s = sum(pandigital_products)