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


scores = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}


def process(inp):
  score1 = 0
  score2 = []
  for i, line in enumerate(inp):
    while True:
      old = line
      line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
      if line == old:
        break
    mismatch = re.findall('[\(\[\{\<][\)\]\}\>]', line)
    if mismatch:
      score1 += scores[mismatch[0][1]][0]
    else:
      s = 0
      line = line[::-1].replace('(', ')').replace('[', ']').replace('{', '}').replace('<', '>')
      for l in line:
        s = (s * 5) + scores[l][1]
      score2.append(s)
  return score1, sorted(score2)[len(score2)//2]



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).splitlines()

  step1_out, step2_out = process(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
