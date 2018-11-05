#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:50:57 2018

@author: toddbilsborough
"""

# Find the sum of all the multiples of 3 or 5 below 1000.

# Direct calculation solution from problem overview
# Gauss's summation formula is n(n+1)/2
# Sums of multiples are p = target / n; (n * p * (p + 1))/2

# Alternate definitionas lambda function
#divisible_under_1000 = lambda n: (n * int((999 / n)) \
#    * (int((999 / n)) + 1)) / 2
                                  
def divisible_under_1000(n):
    p = int(999 / n)
    return (n * p * (p + 1))/2
                                  
sum = divisible_under_1000(3) \
    + divisible_under_1000(5) \
    - divisible_under_1000(15)
    
#print(int(sum))