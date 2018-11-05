#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:54:37 2018

@author: toddbilsborough
"""

# Trying out some built in implementations
# 12.7 ms, so about the same in terms of speed
# But pretty cool in terms of golf code

from math import factorial
digits_sum = sum(map(int, str(factorial(100))))