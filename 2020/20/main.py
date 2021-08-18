#!/bin/env python3

import math

with open('input.txt') as f:
    lines = f.read().strip().split("\n\n")

step1 = 0
step2 = 0

tiles = {}
edges = {}
edges_flipped = {}

for line in lines:
    line = line.split()
    tileid = int(line[1][:-1])
    tiles[tileid] = line[2:]

print(tiles)

def edgetonum(string):
    return int(string.replace('.', '0').replace('#', '1'), 2)

for tileid, tiledata in tiles.items():
    top = tiledata[0]
    right = ''.join(tiledata[i][-1] for i in range(len(tiledata)))
    bottom = tiledata[-1][::-1]
    left = ''.join(tiledata[i][0] for i in range(len(tiledata)))[::-1]
    print(top, right, bottom, left)
    edges[tileid] = [edgetonum(e) for e in [top, right, bottom, left]] + [edgetonum(e[::-1]) for e in [top, right, bottom, left]]

print(edges)

neighbor_count = {}
for tileid, edgearr in edges.items():
    for edge in edgearr:
        for t in edges.keys():
            if t != tileid:
                if edge in edges[t]:
                    neighbor_count[tileid] = neighbor_count.get(tileid, 0) + 1

count_sorted = [i[0] for i in sorted(neighbor_count.items(), key=lambda item: item[1])][:4]
print(count_sorted)
step1 = math.prod(count_sorted)

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
