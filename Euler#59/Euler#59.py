#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:36:02 2018

@author: toddbilsborough
"""

with open("cipher.txt") as f:
    c = f.read()    
cipher = c.split(",")

ascii_low = 97
ascii_high = 122

s = 0

for a in range(ascii_low, ascii_high + 1):
    for b in range(ascii_low, ascii_high + 1):
        for c in range(ascii_low, ascii_high + 1):
            decoded = []
            key = [a, b, c]
            key_index = 0
            for i in range(0, len(cipher)):
                if key_index == 3: key_index = 0
                decoded.append(chr(int(cipher[i]) ^ key[key_index]))
                key_index += 1
            decoded_string = ''.join(decoded)
            if "Gospel" in decoded_string:
                for c in decoded:
                    s += ord(c)