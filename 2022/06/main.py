#!/bin/env python3

import sys
import time

start_time = time.time()

DEBUG = True
frametime = 1/60


def debug(s=''):
  if DEBUG:
    print(s)


def setup(filename):
  with open(filename) as f:
    inp = f.read().strip()
  return inp


def step1(inp):
  for i in range(len(inp)-3):
    visualize(inp, i, 4)
    if len(set(inp[i:i+4])) == 4:
      return i+4
  return None


def step2(inp):
  for i in range(len(inp)-13):
    visualize(inp, i, 14)
    if len(set(inp[i:i+14])) == 14:
      return i+14
  return None


def visualize(inp, start, size):
  sys.stdout.write(f'\033[H\033[J\033[31m{inp[:start]}\033[1m\033[32m{inp[start:start+size]}\033[0m{inp[start+size:]}\n')
  sys.stdout.flush()
  time.sleep(frametime)


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  inp = setup(filename)

  step1_out = step1(inp)
  end_time1 = time.time()

  time.sleep(3)

  step2_out = step2(inp)
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
