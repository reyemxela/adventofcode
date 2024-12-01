#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)

chars = [' ', '█']


def process(inp):
  grid = {}
  nums, folds = inp.split('\n\n')
  step1 = 0
  width = 0
  height = 0

  for num in nums.splitlines():
    x, y = [int(i) for i in num.split(',')]
    width = max(width, x)
    height = max(height, y)
    grid[(x, y)] = 1

  for index, fold in enumerate(folds.splitlines()):
    newgrid = grid.copy()
    coord = int(fold.split('=')[1])

    if fold[11] == 'y':
      for (x, y) in grid.keys():
        if grid[(x, y)] != 1:
          continue
        if y > coord:
          del(newgrid[(x, y)])
          newgrid[(x, height-y)] = 1
      height -= coord+1

    else:
      for (x, y) in grid.keys():
        if grid[(x, y)] != 1:
          continue
        if x > coord:
          del(newgrid[(x, y)])
          newgrid[(width-x, y)] = 1
      width -= coord+1

    grid = newgrid
    if index == 0:
      step1 = len(grid)

  print(f'Step 1: {step1}')
  print('Step 2:')
  print_grid(grid, width, height)


def print_grid(grid, w, h):
  for y in range(h+1):
    for x in range(w+1):
      print(chars[grid.get((x, y), 0)], end='')
    print()
  print()



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  process(inp)



if __name__ == '__main__':
  main()
