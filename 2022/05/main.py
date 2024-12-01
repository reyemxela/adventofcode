#!/bin/env python3

import sys
import time
import shutil
from copy import deepcopy

start_time = time.time()

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)


maxw, maxh = shutil.get_terminal_size()
frametime = 1/60


def setup(filename):
  with open(filename) as f:
    inp = f.read()
  cratestr, procedure = inp.split('\n\n')

  crates = {}
  for line in cratestr.splitlines()[:-1]:
    for i, c in enumerate(line[1::4]):
      if c == ' ':
        continue
      crates.setdefault(i+1, []).append(c)
      
  return crates, procedure


def step1(crates, procedure):
  show_crates(crates)
  for p in procedure.splitlines():
    _, count, _, src, _, dest = p.split()
    for i in range(int(count)):
      crates[int(dest)].insert(0, crates[int(src)].pop(0))
      show_crates(crates)
  return ''.join(crates[k][0] for k in sorted(crates.keys()))


def step2(crates, procedure):
  show_crates(crates)
  for p in procedure.splitlines():
    _, count, _, src, _, dest = p.split()
    crates[int(dest)] = crates[int(src)][:int(count)] + crates[int(dest)]
    del(crates[int(src)][:int(count)])
    show_crates(crates)
  return ''.join(crates[k][0] for k in sorted(crates.keys()))


def show_crates(crates):
  keys = sorted(crates.keys())
  maxlen = max(len(x) for x in crates.values())

  print('\033[2J\033[H', end='')
  print('\n'*(maxh-maxlen-2), end='')
  for y in range(maxlen, 0, -1):
    line = []
    for x in keys:
      l = len(crates[x])
      index = l - y
      if index < 0:
        line.append('   ')
      else:
        line.append(f'[{crates[x][index]}]')
    print(' '.join(line))
  print(' '.join((f' {x} ' for x in keys)))
  time.sleep(frametime)


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  crates, procedure = setup(filename)

  step1_out = step1(deepcopy(crates), procedure)
  end_time1 = time.time()

  time.sleep(3)

  step2_out = step2(deepcopy(crates), procedure)
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
