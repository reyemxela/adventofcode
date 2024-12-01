#!/bin/env python3

import sys
import re

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  inp = increment_password(inp)
  while not check_password(inp):
    inp = increment_password(inp)
  return inp

def increment_password(inp):
  inp = list(inp)
  index = len(inp)-1
  while index >= 0:
    inp[index] = chr(ord(inp[index])+1)
    if inp[index] == '{':
      inp[index] = 'a'
      index -= 1
    else:
      break
  return ''.join(inp)

def check_password(inp):
  if has_straight(inp) and \
     has_good_letters(inp) and \
     has_two_pairs(inp):
    return True
  return False

def has_two_pairs(inp):
  return re.findall(r'([a-z])\1.*([a-z])\2', inp)

def has_good_letters(inp):
  return not re.search('[iol]', inp)

def has_straight(inp):
  for i in range(len(inp)-2):
    if ord(inp[i]) == ord(inp[i+1])-1 == ord(inp[i+2])-2:
      return True
  else:
    return False


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out = step1(inp.strip())
  step2_out = step1(step1_out)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
