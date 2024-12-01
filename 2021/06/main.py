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



def process(inp):
  nums = {}
  for i in inp:
    nums[i] = nums.get(i,0) + 1
  for count in range(256):
    zero = nums.get(0,0)
    for i in range(0, 8):
      nums[i] = nums.get(i+1,0)
    nums[6] += zero
    nums[8] = zero
    if count == 79:
      yield sum(nums.values())
  yield sum(nums.values())



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = list(map(int, readfile(filename).split(',')))

  step1_out, step2_out = process(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
