#!/bin/env python3

import sys
import time

start_time = time.time()

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)


def setup(filename):
  with open(filename) as f:
    inp = f.read()
  
  return inp


def step1(inp):
  total = 0
  for line in inp:
    first, second = line.split(',')
    b1, e1 = map(int, first.split('-'))
    b2, e2 = map(int, second.split('-'))
    if b1 >= b2 and e1 <= e2:
      total += 1
    elif b2 >= b1 and e2 <= e1:
      total += 1
  return total


def step2(inp):
  total = 0
  for line in inp:
    first, second = line.split(',')
    b1, e1 = map(int, first.split('-'))
    b2, e2 = map(int, second.split('-'))
    if b1 >= b2 and b1 <= e2:
      total += 1
    elif b2 >= b1 and b2 <= e1:
      total += 1
  return total


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  inp = setup(filename).splitlines()

  step1_out = step1(inp)
  end_time1 = time.time()

  step2_out = step2(inp)
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
