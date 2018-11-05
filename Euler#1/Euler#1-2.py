#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:33:20 2018

@author: toddbilsborough
"""

sum = 0
x = 5
while x < 1000:
    sum += x
    x += 5
x = 3
while x < 1000:
    if x % 10 == 0 or x % 10 == 5:
        x += 3
    else:
        sum += x
        x += 3    
    
#print(sum)