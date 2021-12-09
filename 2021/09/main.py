#!/bin/env python3

import sys
import math

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)



def process(inp):
  total1 = 0
  totals2 = []
  grid = [list(map(int, x)) for x in inp]
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      low = check_low(grid, x, y)
      total1 += low
      if low > 0:
        totals2.append(fill(grid, x, y))
  return total1, math.prod(sorted(totals2)[-3:])


def check_low(grid, x, y):
  for dy in (-1, 1):
    ny = y+dy
    if ny < 0 or ny >= len(grid):
      continue
    if grid[y][x] >= grid[ny][x]:
      return 0
  for dx in (-1, 1):
    nx = x+dx
    if nx < 0 or nx >= len(grid[y]):
      continue
    if grid[y][x] >= grid[y][nx]:
      return 0
  return 1+grid[y][x]


def fill(grid, x, y, checked=set()):
  debug(f'checking ({x}, {y})')
  if (x, y) in checked:
    debug(f'already checked ({x}, {y})\n')
    return 0
  if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
    return 0
  checked.add((x, y))
  if grid[y][x] == 9:
    return 0
  return 1 + sum(fill(grid, x+dx, y, checked) for dx in (-1, 1)) + sum(fill(grid, x, y+dy, checked) for dy in (-1, 1))


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).splitlines()

  step1_out, step2_out = process(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
