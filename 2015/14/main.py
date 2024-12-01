#!/bin/env python3

import sys

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp



def step1(inp):
  race_time = 2503

  winner = 0
  for line in inp.splitlines():
    line = line.split(' ')

    move_speed = int(line[3])
    move_time = int(line[6])
    rest_time = int(line[13])
    cycle_time = move_time+rest_time

    # get "whole" move cycles
    distance = move_speed*move_time*(race_time//cycle_time)
    # get the ramainder cycle, might be part-way through a move
    distance += (move_speed*min(move_time, race_time%cycle_time))

    if distance > winner:
      winner = distance

  return winner

def step2(inp):
  reindeer = {}
  for line in inp.splitlines():
    line = line.split(' ')

    reindeer[line[0]] = {
      'move_speed': int(line[3]),
      'move_time': int(line[6]),
      'rest_time': int(line[13]),
      'cycle_time': int(line[6]) + int(line[13]),
      'distance': 0,
      'points': 0,
    }

  for second in range(2503):
    for stats in reindeer.values():
      if (second % stats['cycle_time']) < stats['move_time']:
        stats['distance'] += stats['move_speed']
    lead = sorted(reindeer.items(), key=lambda i: i[1]['distance'], reverse=True)
    for r in lead:
      if r[1]['distance'] == lead[0][1]['distance']:
        r[1]['points'] += 1
      else:
        break
  return sorted(reindeer.values(), key=lambda i: i['points'], reverse=True)[0]['points']




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
