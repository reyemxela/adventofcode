#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp


total = 150

def recurse(containers, index=0, subtotal=0, depth=1):
  combos = []

  for i in range(index, len(containers)):
    new_subtotal = subtotal + containers[i]
    if new_subtotal == total:
      combos.append(depth)
    elif new_subtotal < total:
      combos += recurse(containers, i+1, new_subtotal, depth+1)
  return combos



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  containers = list(map(int, inp.splitlines()))
  combos = recurse(containers)
  combos.sort()

  step1_out = len(combos)
  step2_out = combos.count(combos[0])

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
