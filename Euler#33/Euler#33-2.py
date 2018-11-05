#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:31:01 2018

@author: toddbilsborough
"""

# Refined based on math, 12.6 ms

den_product = 1
nom_product = 1

vals = [(i, d, n) for 
        i in range(1, 10) for 
        d in range(1, i) for 
        n in range(1, d)
        if ((n * 10 + i) * d == n * (i * 10 + d))]
for tup in vals:
    den_product *= tup[1]
    nom_product *= tup[2]
    
if (den_product / nom_product) % 1 == 0:
    den_product //= nom_product
    nom_product = 1