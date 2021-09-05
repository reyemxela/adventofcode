#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)


live = '#'
dead = ' '

def step1(inp):
  flipped = []
  for line in inp.splitlines():
    line = line.replace('ne','Xy').\
                replace('sw','xY').\
                replace('nw','y').\
                replace('se','Y').\
                replace('e','X').\
                replace('w','x')
    x = line.count('X') - line.count('x')
    y = line.count('Y') - line.count('y')
    flipped.append((x, y))
    debug(f'{line=} ({x}, {y})')
  debug(f'{len(flipped)=} {flipped=}')
  flipped = [i for i in set(flipped) if flipped.count(i)%2 == 1]
  return flipped, len(flipped)

def step2(flipped):
  grid = {}
  grid.update((t, live) for t in flipped)
  debug(f'i=00{len(grid)=}')
  for i in range(100):
    process(grid)
    debug(f'{i=} {len(grid)=}')
  return len(grid)


def queue_count(grid):
    queue = set()
    for ax, ay in grid.keys():
      queue.update((x, y) for x in (ax-1, ax, ax+1) for y in (ay-1, ay, ay+1))
    return queue

def count_adjacent(grid, cell):
  adj = [    (0, -1), (1, -1),
         (-1, 0),         (1, 0),
             (-1, 1), (0, 1)]
  return sum(int((cell[0]+x, cell[1]+y) in grid.keys()) for x,y in adj)

def process(grid):
    queue = queue_count(grid)
    newlive = []
    newdead = []
    for cell in queue:
        count = count_adjacent(grid, cell)
        if cell in grid.keys():
            if count == 0 or count > 2:
                newdead.append(cell)
        else:
            if count == 2:
                newlive.append(cell)
    for cell in newlive:
        grid[cell] = live
    for cell in newdead:
        if cell in grid.keys():
            del(grid[cell])



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  flipped, step1_out = step1(inp)
  step2_out = step2(flipped)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
