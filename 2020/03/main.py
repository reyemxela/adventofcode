#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().split()


def traverse(map, right, down):
    height = len(map)
    width = len(map[0])

    trees = 0

    for i in range(1, height):
        if (i*down) < height:
            if map[i*down][(i*right)%width] == '#':
                trees += 1
    return trees

step1 = traverse(lines, 3, 1)
print(F"Step 1: {step1}")


step2 = traverse(lines, 1, 1) * traverse(lines, 3, 1) * traverse(lines, 5, 1) * traverse(lines, 7, 1) * traverse(lines, 1, 2)
print(F"Step 2: {step2}")
