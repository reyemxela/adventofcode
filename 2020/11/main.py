#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

step1lines = None
step2lines = None

w = len(lines[0])
h = len(lines)

directions = [ [-1, -1], [0, -1], [1, -1],
               [-1,  0],          [1,  0],
               [-1,  1], [0,  1], [1,  1] ]


def print_grid(grid):
    print(F" {'-'*w}")
    for l in grid:
        print(F"|{l}|")
    print(F" {'-'*w}")

def count_adjacent2(pos, inputlines):
    total = 0
    for dir in directions:
        x,y = pos
        while True:
            x += dir[0]
            y += dir[1]
            if (0 <= x < w) and (0 <= y < h):
                if inputlines[y][x] != '.':
                    total += int(inputlines[y][x] == '#')
                    break
            else:
                break
    #for x in range(pos[0]-1, pos[0]+2):
    #    if 0 <= x < w:
    #        for y in range(pos[1]-1, pos[1]+2):
    #            if 0 <= y < h:
    #                #print(lines[y][x])
    #                if [x, y] != pos:
    #                    total += int(lines[y][x] == '#')
    return total

def count_adjacent(pos, inputlines):
    total = 0
    for x in range(pos[0]-1, pos[0]+2):
        if 0 <= x < w:
            for y in range(pos[1]-1, pos[1]+2):
                if 0 <= y < h:
                    #print(lines[y][x])
                    if [x, y] != pos:
                        total += int(inputlines[y][x] == '#')
    return total
    
def process(inputlines):
    #print_grid(lines)
    newlines = []
    same = False
    for y in range(0, h):
        newline = ''
        for x in range(0, w):
            seat = inputlines[y][x]
            count = count_adjacent([x, y], inputlines)
            #print(F"{[x,y]} - {seat} {count}")
            #print(F"{[x, y]}: {count}")
            if seat == 'L' and count == 0:
                newline += '#'
            elif seat == '#' and count >= 4:
                newline += 'L'
            else:
                newline += seat
        newlines.append(newline)
    if newlines == inputlines: same = True
    return newlines, same

def process2(inputlines):
    #print_grid(lines)
    newlines = []
    same = False
    for y in range(0, h):
        newline = ''
        for x in range(0, w):
            seat = inputlines[y][x]
            count = count_adjacent2([x, y], inputlines)
            #print(F"{[x,y]} - {seat} {count}")
            #print(F"{[x, y]}: {count}")
            if seat == 'L' and count == 0:
                newline += '#'
            elif seat == '#' and count >= 5:
                newline += 'L'
            else:
                newline += seat
        newlines.append(newline)
    if newlines == inputlines: same = True
    return newlines, same


while True:
    if step1lines == None: step1lines = lines.copy()
    step1lines, same = process(step1lines)
    print_grid(step1lines)
    if same:
        break

step1 = ''.join(step1lines).count('#')

while True:
    if step2lines == None: step2lines = lines.copy()
    step2lines, same = process2(step2lines)
    print_grid(step2lines)
    if same:
        break

step2 = ''.join(step2lines).count('#')

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
