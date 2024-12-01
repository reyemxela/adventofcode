#!/bin/env python3

import math

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

target = int(lines[0])
ids = list(map(int, lines[1].replace('x', '-1').split(',')))


besttime = 999
bestid = None

for id in ids:
    if id != -1:
        time = ((int(target/id)+1) * id) - target
        if time < besttime:
            besttime = time
            bestid = id
step1 = bestid*besttime


def modinverse(a, m):
    a = a % m
    for i in range(1,m):
        if ((a * i) % m) == 1:
            return i
    return 1


nums = []
remainders = []
inv = []
pdiv = []
prod = math.prod(i for i in ids if i != -1)
print(prod)
for i, id in enumerate(ids):
    if id != -1:
        nums.append(id)
        remainders.append((id - i) % id)
        pd = int(prod/id)
        pdiv.append(pd)
        inv.append(modinverse(pd, id))
print(nums)
print(remainders)
print(pdiv)
print(inv)

total = 0
for i in range(len(nums)):
    total += remainders[i] * pdiv[i] * inv[i]

step2 = int(total % prod)



print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
