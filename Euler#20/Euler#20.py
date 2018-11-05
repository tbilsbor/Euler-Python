#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:49:18 2018

@author: toddbilsborough
"""

# 12.8 ms and a standard solution

n_factorial = 1
for n in range(2, 101):
    n_factorial *= n
    
sum = 0
while n_factorial > 0:
    sum += n_factorial % 10
    n_factorial //= 10