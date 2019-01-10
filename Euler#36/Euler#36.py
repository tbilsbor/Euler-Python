#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:40:42 2018

@author: toddbilsborough
"""

# 1.32 seconds

def palindrome(n):
    n_str = str(n)
    if len(n_str) % 2 == 0:
        first_half = n_str[0:len(n_str) // 2]
        first_half = first_half[::-1]
        second_half = n_str[len(n_str) // 2:]
        if first_half != second_half: return False
    else:
        first_half = n_str[0:len(n_str) // 2]
        first_half = first_half[::-1]
        second_half = n_str[(len(n_str) // 2) + 1:]
        if first_half != second_half: return False
    return True

def double_palindrome(n):
    if not palindrome(n): return False
    b_n = format(n, 'b')
    if palindrome(b_n): return True

s = 0
for n in range(1, 1000000):
    if double_palindrome(n): s += n