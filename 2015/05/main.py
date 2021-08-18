#!/bin/env python3

import re

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

for l in lines:
    if re.findall(r'ab|cd|pq|xy', l):
        continue
    if len(re.findall(r'[aeiou]', l)) < 3:
        continue
    if not re.findall(r'(\w)\1', l):
        continue
    step1 += 1

for l in lines:
    if not re.findall(r'(\w\w).*\1', l):
        continue
    if not re.findall(r'(\w)\w\1', l):
        continue
    step2 += 1



print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
