#!/bin/env python3

import sys
import collections

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = True

def debug(s=''):
  if DEBUG:
    print(s)



def process(inp):
  template, rulelines = inp.split('\n\n')
  rules = {}
  rules.update(r.split(' -> ') for r in rulelines.splitlines())

  pairs = collections.defaultdict(lambda: 0)
  for i in range(len(template)-1):
    pairs[template[i:i+2]] += 1

  counts = collections.defaultdict(lambda: 0)
  for c in template:
    counts[c] += 1

  for step in range(40):
    new_pairs = pairs.copy()
    for pair, count in pairs.items():
      if count < 1:
        continue
      c = rules[pair]
      new_pairs[pair] -= count
      new_pairs[pair[0] + c] += count
      new_pairs[c + pair[1]] += count
      counts[c] += count
    pairs = new_pairs
    if step == 9:
      yield max(counts.values()) - min(counts.values())
  yield max(counts.values()) - min(counts.values())



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out, step2_out = process(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
