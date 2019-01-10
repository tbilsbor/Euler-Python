#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:32:59 2018

@author: toddbilsborough
"""

# 8.4 seconds

from math import factorial

factorials = list([factorial(n) for n in range(10)])

def sum_of_factorials(n):
    return sum(list([factorials[int(d)] for d in str(n)]))

l = list([n for n in range(3, 2540160) if sum_of_factorials(n) == n])
s = sum(l)