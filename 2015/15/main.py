#!/bin/env python3

import sys
import math

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp


# this solution is definitely not optimized. it takes ~30 seconds
# to run on my laptop. but it does actually work, so...
def step1(inp):
  properties = parse_input(inp)

  best = 0
  best_calories = 0

  # this sucks:
  for i in range(1, 98):
    for j in range(1, 99-i):
      for k in range(1, 100-i-j):
        for l in range(1, 101-i-j-k):
          finalscores = {}

          for prop, ingredients in properties.items():
            for index, (ingredient, score) in enumerate(ingredients.items()):
              finalscores.setdefault(prop, 0)
              finalscores[prop] += (i, j, k, l)[index] * score
          totalscore = math.prod(max(0, s) for (i, s) in finalscores.items() if i != 'calories')

          if finalscores['calories'] == 500:
            if totalscore > best_calories:
              best_calories = totalscore

          if totalscore > best:
            best = totalscore

  return best, best_calories

def step2(inp):
  pass


def parse_input(inp):
  properties = {}
  for line in inp.splitlines():
    ingredient, stats = line.split(': ')
    for prop in stats.split(', '):
      name, score = prop.split(' ')
      properties.setdefault(name, {})[ingredient] = int(score)
  return properties



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out, step2_out = step1(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
