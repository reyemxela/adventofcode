#!/bin/env python3

import sys
import functools

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)



def step1(inp):
  inp.sort()
  best_total = -1
  for n in range(0,inp[-1]):
    total = 0
    for i in inp:
      total += abs(i-n)
    if total < best_total or best_total == -1:
      best_total = total
  return best_total


# checking a range surrounding the average seems to work well for my input,
# added the minimum range of 2 so it would also work for the smaller test input size.
def step2(inp):
  best_total = -1
  avg = sum(inp) // len(inp)
  r = max(len(inp) // 100, 2)
  for n in range(avg-r, avg+r):
    total = 0
    for i in inp:
      total += high_cost(abs(i-n))
    if total < best_total or best_total == -1:
      best_total = total
  return best_total


@functools.lru_cache
def high_cost(n):
  total = 0
  for i in range(n):
    total += i+1
  return total


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = list(map(int,readfile(filename).strip().split(',')))

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
