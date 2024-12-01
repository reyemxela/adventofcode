#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp, matchlist):
  for line in inp.splitlines():
    keep_going = True
    name, info = line.split(': ', 1)
    info = dict(i.split(': ') for i in info.split(', '))

    for item, num in info.items():
      num = int(num)
      if num != matchlist[item]:
        keep_going = False
        break
    else:
      return name

def step2(inp, matchlist):
  greater = ('cats', 'trees')
  less = ('pomeranians', 'goldfish')

  for line in inp.splitlines():
    keep_going = True
    name, info = line.split(': ', 1)
    info = dict(i.split(': ') for i in info.split(', '))

    for item, num in info.items():
      num = int(num)
      if item in greater:
        if num <= matchlist[item]:
          keep_going = False
          break
      elif item in less:
        if num >= matchlist[item]:
          keep_going = False
          break
      elif num != matchlist[item]:
        keep_going = False
        break
    else:
      return name




def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  matchlist = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
  }

  step1_out = step1(inp, matchlist)
  step2_out = step2(inp, matchlist)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
