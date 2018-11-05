#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:12:35 2018

@author: toddbilsborough
"""

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Naive solution
#product = 0
#for a in range(3, 500):
#    for b in range(a + 1, 500):
#        c = 1000 - a - b
#        if a ** 2 + b ** 2 == c ** 2:
#            product = a * b * c

#print(product)

# a + b = 1000 - c
# a = 1000 - b - c
# b = 1000 - a - c
# c = 1000 - a - b

# a = m ** 2 - n ** 2
# b = 2mn
# c = m ** 2 + n ** 2

product = 0
for n in range(1, 22):
    for m in range (n + 1, 22):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a + b + c == 1000:
            product = a * b * c
            break
    if product > 0:
        break

#print(product)