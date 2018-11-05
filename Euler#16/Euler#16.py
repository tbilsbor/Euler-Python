#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:11:00 2018

@author: toddbilsborough
"""

num = 2 ** 1000
sum = 0
while num > 0:
    sum += num % 10
    num //= 10