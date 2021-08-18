#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

for line in lines:
    line = line.split(" (")
    allergens = line[1][:-1].replace(",","").split(" ")[1:]
    for allergen in allergens:
        pass
    print(allergens)




print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
