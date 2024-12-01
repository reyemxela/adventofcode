#!/bin/env python3

import sys
import itertools


def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  return sorted(get_routes(inp))[0]

def step2(inp):
  return sorted(get_routes(inp), reverse=True)[0]


def get_routes(inp):
  cities = set()
  distances = {}
  routes = []

  for line in inp.splitlines():
    items = line.split(' ')
    newcities = tuple(sorted((items[0], items[2])))
    cities.update(newcities)
    distances[newcities] = int(items[4])

  for perm in itertools.permutations(cities):
    distance = 0
    for i in range(len(perm)-1):
      distance += distances[tuple(sorted((perm[i], perm[i+1])))]
    routes.append(distance)
  return routes


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
