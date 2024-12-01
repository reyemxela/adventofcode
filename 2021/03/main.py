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
  line_len = len(inp.split('\n')[0])
  out_len = len(inp.split('\n'))
  inp = inp.replace('\n', '')
  g = ''
  e = ''
  for i in range(line_len):
    l = inp[i::line_len]
    common = int(l.count('1') > l.count('0'))
    g += str(common)
    e += str(1-common)
  return int(g, 2) * int(e, 2)


def step2(inp):
  return life_support(inp, 0) * life_support(inp, 1)


def life_support(inp, mode):
  inplist = inp.split('\n')
  inpstr = inp.replace('\n', '')
  line_len = len(inplist[0])

  common = ''
  for i in range(line_len+1):
    current = [x for x in inplist if x[0:i] == common]
    if len(current) == 1:
      return int(current[0], 2)
    l = ''.join(current)[i::line_len]
    common += str((mode+int(l.count('1') >= l.count('0')))%2)



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
