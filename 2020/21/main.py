#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)

def step1(inp):
  ingredients = []
  allergens = {}

  for line in inp.splitlines():
    ings, alls = line.split(' (contains ')
    ings = ings.split(' ')
    alls = alls.replace(')', '').split(', ')

    ingredients += ings

    for allergen in alls:
      allergens.setdefault(allergen, set(ings)).intersection_update(ings)

  allergen_ings = [i for v in allergens.values() for i in v]
  safe_ings = [i for i in ingredients if i not in allergen_ings]
  debug(f'{allergens=} {ingredients=} {allergen_ings=} {safe_ings=}')
  return allergens, len(safe_ings)

def step2(allergens):
  debug(f'{allergens=}')
  keys = list(allergens.keys())

  while True:
    finished = True
    for i in range(len(keys)):
      v = allergens[keys[i]]
      if len(v) != 1:
        finished = False
      else:
        for j in range(len(keys)):
          if j == i:
            continue
          allergens[keys[j]].difference_update(v)
    if finished:
      break
    debug(f'step2: {allergens}')

  return ','.join(i[1].pop() for i in sorted(allergens.items()))




def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  allergens, step1_out = step1(inp)
  step2_out = step2(allergens)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
