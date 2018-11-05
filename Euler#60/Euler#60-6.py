#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:02:13 2018

@author: toddbilsborough
"""

# Graph theory solution, still really slow

from math import sqrt
import networkx as nx
from networkx.algorithms.clique import find_cliques
   
limit = 100000000
limit_root = int(sqrt(limit))
is_prime = [False, False]
is_prime += [True for n in range(2, limit_root + 1)]

for p in range(2, limit_root + 1):
    if is_prime[p]:
        c = p * p
        while c <= limit_root:
            is_prime[c] = False
            c += p
         
def check_prime(n):
    if n < limit_root: return is_prime[n]
    n_root = int(sqrt(n))
    for f in filter(lambda i: is_prime[i], range(3, n_root + 1)):
        if n % f == 0:
            return False
    return True

def check_concatenation(n, p):
    concat = int(str(p) + str(n))
    if not check_prime(concat):
        return False
    concat = int(str(n) + str(p))
    if not check_prime(concat):
        return False
    return True

pairs = []
primes = list(filter(lambda i: is_prime[i], range(3, 10001)))
for p in primes:
    for q in filter(lambda x: x > p, primes):
        pairs.append([p, q])
    
prime_pairs = []    
for pair in pairs:
    if check_concatenation(pair[0], pair[1]): prime_pairs.append(pair)
        
G = nx.Graph()
G.add_edges_from(prime_pairs)
five_cliques = [clique for clique in find_cliques(G) if len(clique)==5]

#%%

s = min(list(sum(clq) for clq in five_cliques))