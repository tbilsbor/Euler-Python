#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:27:58 2018

@author: toddbilsborough
"""

# doesn't keep all the numbers
# 49.2 ms

a = 1
b = 1
c = 1
i = 2
while len(str(c)) < 1000:
    c = a + b
    a = b
    b = c
    i += 1