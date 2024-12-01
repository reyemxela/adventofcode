#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

width = 100
height = 100

live = '#'
dead = '.'

def step1(inp):
  grid = generate_grid(inp)
  print_grid(grid)
  for i in range(100):
    process(grid)
    print_grid(grid)
  return len(grid)

def step2(inp):
  grid = generate_grid(inp)
  stuck_on(grid)
  print_grid(grid)
  for i in range(100):
    process(grid)
    stuck_on(grid)
    print_grid(grid)
  return len(grid)


def stuck_on(grid):
  grid[(0,0)] = grid[(0,99)] = grid[(99,0)] = grid[(99,99)] = live

def generate_grid(inp):
  grid = {}
  for y, line in enumerate(inp.splitlines()):
    for x, char in enumerate(line):
      if char == live:
        grid[(x,y)] = live
  return grid

def queue_count(grid):
    queue = set()
    for ax, ay in grid.keys():
      queue.update((x%width, y%height) for x in (ax-1, ax, ax+1) for y in (ay-1, ay, ay+1))
    return queue

def count_adjacent(grid, cell):
  adj = [(-1, -1), (-1, 0), (-1, 1),
         (0, -1),           (0, 1),
         (1, -1),  (1, 0),  (1, 1)]
  return sum(int((cell[0]+x, cell[1]+y) in grid.keys()) for x,y in adj)

def process(grid):
    queue = queue_count(grid)
    newlive = []
    newdead = []
    for cell in queue:
        count = count_adjacent(grid, cell)
        if cell in grid.keys():
            if count in (2, 3):
                newlive.append(cell)
            else:
                newdead.append(cell)
        else:
            if count == 3:
                newlive.append(cell)
            else:
                newdead.append(cell)
    for cell in newlive:
        grid[cell] = live
    for cell in newdead:
        if cell in grid.keys():
            del(grid[cell])

def print_grid(grid):
  for y in range(height):
    for x in range(width):
      print(grid.get((x,y), dead), end='')
    print()


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
