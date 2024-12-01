#!/bin/env python3

import sys
import re
from functools import cache

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp


def step1(inp):
  return recurse(inp, findwire(inp, 'a'))


def step2(inp, override):
  inp = re.sub('.*-> b\n', f'{override} -> b\n', inp)
  return step1(inp)


def findwire(inp, wire):
  return re.search(f'(.*-> {wire})\n', inp).group(1).split(' -> ')[0]

@cache
def recurse(inp, instr):
  expr = ''

  for i in instr.split(' '):
    if str(i).isalpha():
      i = recurse(inp, findwire(inp, i))
    expr += str(i)

  return eval(expr)


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  inp = inp.replace("AND", "&").replace("OR", "|").replace("LSHIFT", "<<").replace("RSHIFT", ">>").replace("NOT", "65535 -")

  step1_out = step1(inp)
  step2_out = step2(inp, step1_out)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()






##!/bin/env python3
#
#import re
#
#with open('input.txt') as f:
#    lines = f.read().splitlines()
#
#step1 = 0
#step2 = 0
#
#signals = {}
#
#for l in lines:
#    inp, out = l.split(" -> ")
#
#    inp = re.sub(r"([a-z]+)", r"signals['\1']", inp)
#
#    inp = inp.replace("AND", "&").replace("OR", "|").replace("LSHIFT", "<<").replace("RSHIFT", ">>").replace("NOT", "65535 -")
#    print(F"{out} = {inp}")
#    signals[out] = eval(inp)
#
#print(signals['a'])
#
#
#
#
#print(F"Step 1: {step1}")
#print(F"Step 2: {step2}")
