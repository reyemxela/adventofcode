#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  return run_program(inp)['b']

def step2(inp):
  return run_program(inp, a=1)['b']


def run_program(inp, a=0, b=0):
  lines = inp.splitlines()
  ptr = 0
  r = {'a': a, 'b': b}

  while True:
    if ptr >= len(lines):
      break

    instr, *args = lines[ptr].replace(',', '').split(' ')
    if   instr == 'hlf':
      r[args[0]] //= 2
      ptr += 1
    elif instr == 'tpl':
      r[args[0]] *= 3
      ptr += 1
    elif instr == 'inc':
      r[args[0]] += 1
      ptr += 1
    elif instr == 'jmp':
      ptr += int(args[0])
    elif instr == 'jie':
      if r[args[0]] % 2 == 0:
        ptr += int(args[1])
      else :
        ptr += 1
    elif instr == 'jio':
      if r[args[0]] == 1:
        ptr += int(args[1])
      else :
        ptr += 1
  return r

    


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
