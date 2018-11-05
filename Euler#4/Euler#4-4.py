#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:14:33 2018

@author: toddbilsborough
"""

# Further improvements

# The palindrome must be 6 digits:
# 999 * 999 is six digits and 111111 is the smallest six-digit palindrome
# P=11(9091x * 910y * 100z)
# So one of the numbers must have 11 has a factor
# Down to 15.2 ms from 25.6

# Tweaks and refinements bring it down to 14.9

def reverse(n):
    return int(str(n)[::-1])

def isPalindrome(n):
    return n == reverse(n)

largest = -1
for a in range(999, 100, -1):
    b = a
    while b % 11 != 0: b -= 1
    while b >= 100:
        product = a * b
        if product < largest:
            break
        if isPalindrome(product) and product > largest:
            largest = product
            break
        b -= 11
            
#print(largest)