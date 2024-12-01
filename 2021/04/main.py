#!/bin/env python3

import sys
import re

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)



def process(inp):
  wins = []
  nums = list(map(int, inp[0].split(',')))
  boards = [list(map(int, re.findall('\d+', inp[i]))) for i in range(1, len(inp))]
  for n in nums:
    for b in boards:
      if n in b:
        b[b.index(n)] = True
        if check_board(b):
          wins.append(sum(x for x in b if type(x) == int) * n)
          boards[boards.index(b)] = []
          if boards == [[]]*len(boards):
            return wins[0], wins[-1]


def check_board(board):
  for i in range(0, 5):
    if all(x == True for x in board[i::5]):
      return True
  for i in range(0, 21, 5):
    if all(x == True for x in board[i:i+5]):
      return True


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).split('\n\n')

  step1_out, step2_out = process(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
