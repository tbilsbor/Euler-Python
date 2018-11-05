#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:33:20 2018

@author: toddbilsborough
"""

sum = 0
for x in range(3, 1000):
    if x % 3 == 0 or x % 5 == 0: sum += x  
    
#print(sum)