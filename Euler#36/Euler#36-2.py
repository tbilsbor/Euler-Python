#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:40:42 2018

@author: toddbilsborough
"""

# 874 ms

def palindrome(n):
    return str(n) == str(n)[::-1]

def double_palindrome(n):
    if not palindrome(n): return False
    b_n = format(n, 'b')
    if palindrome(b_n): return True

s = sum([n for n in range(1, 1000000) if double_palindrome(n)])