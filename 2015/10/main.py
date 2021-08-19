#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  inp = inp.strip()
  for i in range(40):
    inp = parse(inp)
  return len(inp)

def step2(inp):
  inp = inp.strip()
  for i in range(50):
    inp = parse(inp)
  return len(inp)


def parse(inp):
  currentnum = inp[0]
  currentlen = 1
  output = ''

  for index in range(1, len(inp)):
    if inp[index] != currentnum:
      output += str(currentlen) + currentnum
      currentlen = 1
      currentnum = inp[index]
    else:
      currentlen += 1
  output += str(currentlen) + currentnum
  return output


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
