#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:41:36 2018

@author: toddbilsborough
"""

limit = 1000000
is_prime = [True for n in range(limit)]
is_prime[0] = False
is_prime[1] = False
for i in range(limit):
    if not is_prime[i]:
        continue
    c = i
    while c < limit - i:
        c += i
        is_prime[c] = False