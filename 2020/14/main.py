#!/bin/env python3

import re

with open('input.txt') as f:
    lines = f.read().split('mask = ')[1:]

step1 = 0
step2 = 0

mem = {}

for l in lines:
    l = l.splitlines()
    mask = l[0]
    commands = l[1:]

    for c in commands:
        addr, value = re.split('\[(.*)\] = (.*)', c)[1:3]
        value = F"{int(value):036b}"
        mem[addr] = ''.join(value[i] if mask[i] == 'X' else mask[i] for i in range(36))

step1 = sum(int(v, 2) for v in mem.values())

mem = {}

for l in lines:
    l = l.splitlines()
    mask = l[0]
    commands = l[1:]

    for c in commands:
        addr, value = re.split('\[(.*)\] = (.*)', c)[1:3]
        addr = F"{int(addr):036b}"
        addr = ''.join(mask[i] if mask[i] in ['X', '1'] else addr[i] for i in range(36))

        numx = addr.count('X')
        for n in range(2**numx):
            combo = list(F"{n:0{numx}b}")
            a = ''.join(combo.pop() if addr[i] == 'X' else addr[i] for i in range(36))
            mem[int(a, 2)] = value

step2 = sum(map(int, mem.values()))

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
