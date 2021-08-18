#!/bin/env python3

with open('input.txt') as f:
    lines = f.read()

step1 = 0
step2 = 0

for l in lines.splitlines():
    dim = list(map(int, l.split("x")))
    dim.sort()
    step1 += (3 * dim[0]*dim[1]) + 2 * (dim[1]*dim[2] + dim[2]*dim[0])
    step2 += (2 * (dim[0] + dim[1])) + (dim[0]*dim[1]*dim[2])



print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
