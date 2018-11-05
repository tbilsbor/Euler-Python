#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:39:48 2018

@author: toddbilsborough
"""

s = sum([num for num in range(2, 354395) if 
           num == sum([int(c)**5 for c in str(num)])])