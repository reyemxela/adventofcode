#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  return codecount(inp) - valuecount(inp)

def step2(inp):
  return encodedcount(inp) - codecount(inp)


def codecount(inp):
  return len(inp.replace('\n', ''))

def valuecount(inp):
  return len(''.join(map(eval, inp.splitlines())))

def encodedcount(inp):
  return codecount(inp) + inp.count('"') + inp.count('\\') + (len(inp.splitlines())*2)

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
