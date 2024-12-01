#!/bin/env python3

import sys
import itertools

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(people):
  return get_optimal_seating(people)


def step2(people):
  people['Me'] = {}
  for p in people.keys():
    people[p]['Me'] = 0
    people['Me'][p] = 0
  
  return get_optimal_seating(people)


def parse_people(inp):
  people = {}
  for line in inp.splitlines():
    line = line.split(' ')

    p1, p2 = line[0], line[10].strip('.')
    num = int(line[3]) * (1 if line[2] == 'gain' else -1)

    people.setdefault(p1, {})[p2] = num
  return people

def get_optimal_seating(people):
  highest = 0
  for order in itertools.permutations(people.keys()):
    happiness = 0
    for i in range(len(order)):
      j = (i+1) % len(order)
      num1 = people[order[i]][order[j]]
      num2 = people[order[j]][order[i]]
      happiness += num1 + num2
    if happiness > highest:
      highest = happiness
  return highest


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  people = parse_people(inp)
  step1_out = step1(people)
  step2_out = step2(people)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
