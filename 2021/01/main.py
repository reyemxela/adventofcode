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
  count = 0
  for i in range(len(inp)-1):
    count += int(inp[i] < inp[i+1])
  return count

def step2(inp):
  count = 0
  for i in range(len(inp)-3):
    cur = sum(inp[i:i+3])
    count += int(sum(inp[i:i+3]) < sum(inp[i+1:i+4]))
  return count


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = list(map(int, readfile(filename).splitlines()))

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
