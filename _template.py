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


def step1(inp):
  return None


def step2(inp):
  return None




def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  inp = setup(filename)

  step1_out = step1(inp)
  end_time1 = time.time()

  step2_out = step2(inp)
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
