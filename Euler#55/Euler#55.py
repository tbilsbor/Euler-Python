#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:51:15 2018

@author: toddbilsborough
"""

# How many Lychrel numbers are there below ten-thousand?
# Runs in 275 ms
# Down to 127 ms by using int(str(n)[::-1]) for reversal

def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse(n)

def is_lychrel(n):
    iterations = 0
    while not is_palindrome(n + reverse(n)):
        n += reverse(n)
        iterations += 1
        if iterations >= 50:
            return True
    return False

count= 0
for n in range(1, 10001):
    if is_lychrel(n): count += 1

print(count)