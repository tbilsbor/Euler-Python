#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:56:53 2018

@author: toddbilsborough
"""

#How many distinct terms are in the sequence 
# generated by a ** b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

terms = len(set([a ** b for a in range(2, 101) for b in range(2, 101)]))