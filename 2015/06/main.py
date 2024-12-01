#!/bin/env python3

import numpy as np

with open('input.txt') as f:
    lines = f.read().replace('turn ', '').splitlines()

step1 = 0
step2 = 0

doprint = False

grid = np.zeros([1000, 1000], dtype=np.int64)
grid2 = np.zeros([1000, 1000], dtype=np.int64)

def printgrid(inputgrid):
    for y in range(0, 1000, 10):
        newline = ''
        for x in range(0, 1000, 10):
            newline += "#" if inputgrid[y, x] else " "
        print(newline)

commands = {"on": 1, "off": -1, "toggle": 2}

for l in lines:
    l = l.split()
    x1, y1 = map(int, l[1].split(','))
    x2, y2 = map(int, l[3].split(','))
    command = l[0]

    section = grid[y1:y2+1, x1:x2+1]
    if command == "toggle":
        section[:] = 1-section
    elif command == "on":
        section[:] = 1
    elif command == "off":
       section[:] = 0

    section2 = grid2[y1:y2+1, x1:x2+1]
    section2[:] += commands[command]
    section2[:] = section2*(section2>0)

    if doprint:
        printgrid(grid)


step1 = np.sum(grid)
step2 = np.sum(grid2)

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
