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
    inp = f.readlines()
  
  return inp

lose = 0
tie = 3
win = 6

rock = 1
paper = 2
scissors = 3

def step1(inp):
  SCORES = {
    "A X": tie  + rock,       # Rock     - Rock
    "A Y": win  + paper,      # Rock     - Paper
    "A Z": lose + scissors,   # Rock     - Scissors
    "B X": lose + rock,       # Paper    - Rock
    "B Y": tie  + paper,      # Paper    - Paper
    "B Z": win  + scissors,   # Paper    - Scissors
    "C X": win  + rock,       # Scissors - Rock
    "C Y": lose + paper,      # Scissors - Paper
    "C Z": tie  + scissors,   # Scissors - Scissors
  }
  score = 0
  for line in inp:
    score += SCORES[line.strip()]
  return score


def step2(inp):
  SCORES = {
    "A X": lose + scissors,   # Rock     - Lose
    "A Y": tie  + rock,       # Rock     - Tie
    "A Z": win  + paper,      # Rock     - Win
    "B X": lose + rock,       # Paper    - Lose
    "B Y": tie  + paper,      # Paper    - Tie
    "B Z": win  + scissors,   # Paper    - Win
    "C X": lose + paper,      # Scissors - Lose
    "C Y": tie  + scissors,   # Scissors - Tie
    "C Z": win  + rock,       # Scissors - Win
  }
  score = 0
  for line in inp:
    score += SCORES[line.strip()]
  return score


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
