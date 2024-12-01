#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().split("\n\n")


step1 = 0
step2 = 0


for line in lines:
    seen = ""
    for l in line.replace("\n", ""):
        if l not in seen:
            seen += l
    step1 += len(seen)

for line in lines:
    line = line.strip().replace("\n", " ")
    numpeople = len(line.split(" "))
    for l in line.split(" ")[0]:
        if line.count(l) == numpeople:
            step2 += 1


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
