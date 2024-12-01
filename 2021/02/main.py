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



def step1(inp):
  pos1 = 0
  pos2 = 0
  depth1 = 0
  depth2 = 0
  aim2 = 0

  for l in inp:
    d, a = l.split(' ')
    a = int(a)
    if d == 'forward':
      pos1 += a
      pos2 += a
      depth2 += a*aim2
    elif d == 'down':
      depth1 += a
      aim2 += a
    else:
      depth1 -= a
      aim2 -= a
  return pos1*depth1, pos2*depth2



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).splitlines()

  step1_out, step2_out = step1(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
