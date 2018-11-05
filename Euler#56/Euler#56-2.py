#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:17:34 2018

@author: toddbilsborough
"""

# Considering natural numbers of the form, ab, where a, b < 100, 
# what is the maximum digital sum?

# Investigation

#def get_digital_sum(n):
#    d_sum = 0
#    while n > 0:
#        d_sum += n % 10
#        n //= 10
#    return d_sum
#
#for a in range(1, 6):
#    for b in range(1, 6):
#        n = a ** b
#        digital_sum = get_digital_sum(n)
#        print("%s ** %s = %s, sum of %s" % (str(a), str(b), 
#                                            str(n), str(digital_sum)))
#        
#largest = -1
#largest_a = -1
#largest_b = -1
#for a in range(99, 0, -1):
#    for b in range(99, 0, -1):
#        n = a ** b
#        digital_sum = get_digital_sum(n)
#        if digital_sum > largest:
#            largest = digital_sum
#            largest_a = a
#            largest_b = b
#        
#print("%s ** %s = %s, sum of %s" % (str(largest_a), 
#                                    str(largest_b),
#                                    str(largest_a ** largest_b),
#                                    str(largest)))

for n in [8 ** x for x in range(1, 10)]:
    print(n)