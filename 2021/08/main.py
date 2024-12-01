#!/bin/env python3

import sys
import re

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)


def step1(inp):
  outlen = 0
  for line in inp:
    out = line.split(' | ')[1]
    outlen += len([x for x in out.split(' ') if len(x) in (2, 4, 3, 7)])
  return outlen


def step2(inp):
  total = 0
  for line in inp:
    digits, out = line.split(' | ')
    digits = digits.split()
    out = out.split()

    solved = [None]*10
    solved[1] = find(digits, 2) # \ these are the easy ones.
    solved[7] = find(digits, 3) # | they're just matched
    solved[4] = find(digits, 4) # | to their length.
    solved[8] = find(digits, 7) # /
    solved[3] = find(digits, 3, solved[1]) # 3 digit minus 1 digit leaves 3 segments
    solved[9] = find(digits, 0, solved[3]+solved[4]) # combine 3 and 4 to make 9
    solved[5] = find(digits, 1, solved[9]) # 9 minus 5 leaves 1
    solved[2] = find(digits, 5) # 2 is the last 5-length digit
    solved[6] = find(digits, 1, solved[5]) # 6 minus 5 leaves 1
    solved[0] = find(digits, 6) # 0 is the only one left, with 6 segments

    total += int(''.join(str(solved.index(''.join(sorted(x)))) for x in out))
  return total


# this whole thing works by making sets of the input string and each remaining possibility,
# taking the intersection of those sets (to remove what's in common), and matching the number
# of characters remaining against matchlen
def find(digits, matchlen, diff=''):
  match = [x for x in digits if len(set(x) ^ set(diff)) == matchlen]
  digits.remove(match[0])
  return ''.join(sorted(match[0]))



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).splitlines()

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
