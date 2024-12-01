#!/bin/env python3

import sys
import time

start_time = time.time()

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)


def setup(filename):
  with open(filename) as f:
    inp = f.read()
  
  return inp


def get_score(letter):
  score = ord(letter)
  if score < 91:
    score -= 38
  else:
    score -= 96
  return score

def step1(inp):
  total = 0
  for line in inp:
    half = len(line)//2
    first, second = line[:half], line[half:]
    common = (set(first) & set(second)).pop()
    total += get_score(common)
  return total


def step2(inp):
  total = 0
  for i in range(0, len(inp), 3):
    common = (set(inp[i]) & set(inp[i+1]) & set(inp[i+2])).pop()
    total += get_score(common)
  return total




def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  inp = setup(filename).splitlines()

  step1_out = step1(inp)
  end_time1 = time.time()

  step2_out = step2(inp)
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
