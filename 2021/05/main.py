#!/bin/env python3

import sys
from math import copysign

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)



def step1(inp):
  coords = {}
  for l in inp:
    (x1, y1), (x2, y2) = map(lambda x: (int(x[0]),int(x[1])), map(lambda x: x.split(','), l.split(' -> ')))
    if x1 == x2 or y1 == y2:
      for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
          coords[(x,y)] = coords.get((x,y), 0) + 1
          debug(f'{x=} {y=}')
  return coords, len(list(filter(lambda x: x > 1, coords.values())))


def step2(inp, coords):
  for l in inp:
    (x1, y1), (x2, y2) = map(lambda x: (int(x[0]),int(x[1])), map(lambda x: x.split(','), l.split(' -> ')))
    if x1 != x2 and y1 != y2:
      dx = int(copysign(1, x2-x1))
      dy = int(copysign(1, y2-y1))
      for i in range(abs(x1-x2)+1):
        x = x1+(i*dx)
        y = y1+(i*dy)
        coords[(x,y)] = coords.get((x,y), 0) + 1
        debug(f'{x=} {y=}')
  return len(list(filter(lambda x: x > 1, coords.values())))




def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).strip().splitlines()

  coords, step1_out = step1(inp)
  step2_out = step2(inp, coords)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
