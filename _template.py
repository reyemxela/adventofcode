#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  pass

def step2(inp):
  pass




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
