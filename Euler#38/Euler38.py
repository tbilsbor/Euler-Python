#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:26:31 2019

@author: toddbilsborough
"""

# 113 ms

from itertools import permutations
    
for perm in (p for p in list(permutations("123456789", 9))[::-1]):
    perm_str = ''.join(perm)
    if int(perm_str[0:4]) * 2 == int(perm_str[4:]): break