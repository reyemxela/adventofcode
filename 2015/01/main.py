#!/bin/env python3

with open('input.txt') as f:
    lines = f.read()

step1 = 0
step2 = 0

count = 0
for i in lines.strip():
    count += 1
    if i == '(':
        step1 += 1
    else:
        step1 -= 1
    if step2 == 0 and step1 == -1:
        step2 = count

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
