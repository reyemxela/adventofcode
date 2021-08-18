#!/bin/env python3

import math

with open('input.txt') as f:
    lines = list(map(int, f.read().splitlines()))

lines.insert(0,0)
lines.sort()
lines.append(lines[-1]+3)

step1 = 0
step2 = 0

differences = {1:0, 2:0, 3:0}

for i in range(len(lines)-1):
    diff = lines[i+1] - lines[i]
    differences[diff] += 1

step1 = differences[1] * differences[3]

cache = {}

def find_combinations(depth=0):
    total = 0
    if depth < len(lines):
        if depth not in cache.keys():
            for i in range(depth+1, depth+4):
                if i < len(lines):
                    if lines[i] - lines[depth] <= 3:
                        total += find_combinations(i)
                if i == len(lines):
                    total = 1
                    break
            cache[depth] = total
        else: total = cache[depth]
    #print(total)
    return total

#def valid_combination(l):
#    for i in range(len(l)-1):
#        if l[i+1] - l[i] > 3:
#            return False
#    return True

#totalcombos = []
#for i in range(len(lines)-2):
#    combos = 0
#    for j in range(1,3):
#        if lines[i+j] - lines[i] <= 3:
#            combos += 1
#    totalcombos.append(combos)
#print(totalcombos)
#
#step2 = math.prod(totalcombos)

step2 = find_combinations()
#step2 = combo2(lines)
    




print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
