#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

dead = None
live = 1


# { z
#  y
#  ['.#.', x
#   '..#',
#   '###']
# }


grid = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            grid[(x, y, 0)] = live
#grid[0] = lines

grid2 = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            grid2[(x, y, 0, 0)] = live

minz, maxz = [-1, 2]
miny, maxy = [-1, len(lines)+1]
minx, maxx = [-1, len(lines[0])+1]

def print_grid(inputgrid):
    for y in range(miny, maxy):
        for z in range(minz, maxz):
            for x in range(minx, maxx):
                print("#" if inputgrid.get((x, y, z)) == live else ".", end='')
            print("   ", end='')
        print()
    print("\n\n")


def count_adjacent2(pos, inputgrid):
    total = 0
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            for z in range(pos[2]-1, pos[2]+2):
                for w in range(pos[3]-1, pos[3]+2):
                    if [x, y, z, w] != pos:
                        total += int(inputgrid.get((x, y, z, w), None) == live)
    return total

def count_adjacent(pos, inputgrid):
    total = 0
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            for z in range(pos[2]-1, pos[2]+2):
                if [x, y, z] != pos:
                    total += int(inputgrid.get((x, y, z), None) == live)
    return total


for i in range(6):
    print_grid(grid)
    newgrid = grid.copy()
    for z in range(minz, maxz):
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                cell = grid.get((x, y, z), dead)
                count = count_adjacent([x, y, z], grid)
                if cell == live and count not in [2,3]:
                    del(newgrid[(x, y, z)])
                elif cell != live and count == 3:
                    newgrid[(x, y, z)] = live
                #print(F"{(x, y, z)}: {count}")
    grid = newgrid
    minz -= 1
    maxz += 1
    miny -= 1
    maxy += 1
    minx -= 1
    maxx += 1

#print(grid)
step1 = len(grid)

minw, maxw = [-1, 2]
minz, maxz = [-1, 2]
miny, maxy = [-1, len(lines)+1]
minx, maxx = [-1, len(lines[0])+1]


for i in range(6):
    #print_grid(grid2)
    newgrid = grid2.copy()
    for w in range(minw, maxw):
        for z in range(minz, maxz):
            for y in range(miny, maxy):
                for x in range(minx, maxx):
                    cell = grid2.get((x, y, z, w), dead)
                    count = count_adjacent2([x, y, z, w], grid2)
                    if cell == live and count not in [2,3]:
                        del(newgrid[(x, y, z, w)])
                    elif cell != live and count == 3:
                        newgrid[(x, y, z, w)] = live
                    #print(F"{(x, y, z)}: {count}")
    grid2 = newgrid
    minw -= 1
    maxw += 1
    minz -= 1
    maxz += 1
    miny -= 1
    maxy += 1
    minx -= 1
    maxx += 1

#print(grid2)
step2 = len(grid2)

d = [0,1]
h = len(lines)
w = len(lines[0])


def expand_grid(inputgrid):
    global w, h, d
    w += 2
    h += 2
    d[0] -= 1
    d[1] += 1
    for z in range(d[0], d[1]):
        if z not in inputgrid.keys():
            inputgrid[z] = [dead * w] * h
        else:
            inputgrid[z] =  [dead * w] + [dead + l + dead for l in inputgrid[z]] + [dead * w]
    #print_grid(inputgrid)
    return inputgrid


def process(inputgrid):
    inputgrid = expand_grid(inputgrid)
    countgrid = inputgrid.copy()
    for z in range(d[0], d[1]):
        newlines = []
        countlines = []
        for y in range(0, h):
            newline = ''
            countline = ''
            for x in range(0, w):
                cell = inputgrid[z][y][x]
                count = count_adjacent([x, y, z], inputgrid)
                #print([x, y, z], count)
                if cell == live and count in [2,3]:
                    newline += live
                elif cell == dead and count == 3:
                    newline += live
                else:
                    newline += dead
                countline += str(count)
            newlines.append(newline)
            countlines.append(countline)
        inputgrid[z] = newlines
        countgrid[z] = countlines
    print_grid(countgrid)
    return inputgrid


#for i in range(2):
#    print_grid(grid)
#    grid = process(grid)
    
#directions = [ [-1, -1], [0, -1], [1, -1],
#               [-1,  0],          [1,  0],
#               [-1,  1], [0,  1], [1,  1] ]

#def count_adjacent2(pos, inputlines):
#    total = 0
#    for dir in directions:
#        x,y = pos
#        while True:
#            x += dir[0]
#            y += dir[1]
#            if (0 <= x < w) and (0 <= y < h):
#                if inputlines[y][x] != '.':
#                    total += int(inputlines[y][x] == '#')
#                    break
#            else:
#                break
#    #for x in range(pos[0]-1, pos[0]+2):
#    #    if 0 <= x < w:
#    #        for y in range(pos[1]-1, pos[1]+2):
#    #            if 0 <= y < h:
#    #                #print(lines[y][x])
#    #                if [x, y] != pos:
#    #                    total += int(lines[y][x] == '#')
#    return total

#def process2(inputlines):
#    #print_grid(lines)
#    newlines = []
#    same = False
#    for y in range(0, h):
#        newline = ''
#        for x in range(0, w):
#            seat = inputlines[y][x]
#            count = count_adjacent2([x, y], inputlines)
#            #print(F"{[x,y]} - {seat} {count}")
#            #print(F"{[x, y]}: {count}")
#            if seat == 'L' and count == 0:
#                newline += '#'
#            elif seat == '#' and count >= 5:
#                newline += 'L'
#            else:
#                newline += seat
#        newlines.append(newline)
#    if newlines == inputlines: same = True
#    return newlines, same


#while True:
#    if step1lines == None: step1lines = lines.copy()
#    step1lines, same = process(step1lines)
#    print_grid(step1lines)
#    if same:
#        break
#
#step1 = ''.join(step1lines).count('#')
#
#while True:
#    if step2lines == None: step2lines = lines.copy()
#    step2lines, same = process2(step2lines)
#    print_grid(step2lines)
#    if same:
#        break
#
#step2 = ''.join(step2lines).count('#')

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
