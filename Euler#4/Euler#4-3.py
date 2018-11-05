#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:05:53 2018

@author: toddbilsborough
"""

# Further improvements
# Palindromality is determined by function
# Breaks from the inner loop if the results are less than largest
# Down to 25.6 ms from 1.52 s

def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n //= 10
    return reversed

def isPalindrome(n):
    return n == reverse(n)

largest = -1
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        product = a * b
        if product < largest:
            break
        if isPalindrome(product) and product > largest:
            largest = product
            
#print(largest)