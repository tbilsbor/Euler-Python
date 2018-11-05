#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:27:58 2018

@author: toddbilsborough
"""

# 48.5 ms, brute force through iteration, about as efficient as it gets

fib = [1, 1]
i = 2
while len(str(fib[-1])) < 1000:
    fib.append(fib[i - 1] + fib[i - 2])
    i += 1