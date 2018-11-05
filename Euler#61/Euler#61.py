#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:44:20 2018

@author: toddbilsborough
"""

# Solution to Euler 61, runs in 70.2 ms
# Generates a digraph of all figural numbers labeled by category
# Edges are drawn between connected pairs of figural numbers (eg 8128 and 2882)
# Successions are parsed recursively until a solution is found

import networkx as nx
import matplotlib.pyplot as plt

# List of lists for the different figural categories
figural = [[1], [1], [1], [1], [1], [1]]

# Generate figural numbers
n = 2
step = 1
while ((n * (n - 1)) / 2) < 10000:
    for i in range(0, 6):
        num = n + (step * (i + 1))
        figural[i].append(num)
    step = figural[0][-1]
    n += 1

# Get rid of figural numbers less than or greater than 4 digits    
for i in range(0, 6):
    figural[i] = [x for x in figural[i] if x > 1000 and x < 10000]

# Initiate graph    
G = nx.DiGraph()

# Add nodes
# Each node is labeled based on which figure it came from
for i in range(0, 6):
    G.add_nodes_from(figural[i], fig=i)

# Add edges
for i in range(0, 6):
    for j in range(0, len(figural[i])):
        second_half = figural[i][j] % 100
        for k in [x for x in range(0, 6) if x != i]:
            for m in range(0, len(figural[k])):
                first_half = figural[k][m] // 100
                if second_half == first_half:
                    G.add_edge(figural[i][j], figural[k][m])
                    
# Holds whether a given figure is already represented in a succession path
repped = [False for x in range(0, 6)] 
# Holds the path while it's being tested
path = []

def get_path(node):
    # If it's at 5, check for the next one based on it linking back up with
    # the first one
    if len(path) == 5:
        for n in G.successors(node):
            if path[0] in G.successors(n) and \
            repped[G.nodes[n]['fig']] == False:
                repped[G.nodes[n]['fig']] = True
                path.append(n)
                return
        return
    # Otherwise just test out the successions recursively
    for n in G.successors(node):
        if repped[G.nodes[n]['fig']] == True: continue
        path.append(n)
        repped[G.nodes[n]['fig']] = True
        get_path(n)
        if len(path) == 6:
            return
        path.remove(path[-1])
        repped[G.nodes[n]['fig']] = False

# Tests for paths starting on every node
for node in G:
    repped = [False for x in range(0, 6)]
    path = []
    path.append(node)
    repped[G.nodes[node]['fig']] = True
    get_path(node)
    if len(path) == 6:
        break
    
s = sum(path)

nx.draw(G, with_labels=True, font_weight='bold')