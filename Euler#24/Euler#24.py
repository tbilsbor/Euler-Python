#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:05:06 2018

@author: toddbilsborough
"""

# Testing with python's itertools
# About 1s run time

from itertools import permutations

perms = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
perms = sorted(perms)
millionth = perms[999999]