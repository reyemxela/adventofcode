#!/bin/env python3

import sys
import time

start_time = time.time()

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)


def setup(filename):
  with open(filename) as f:
    inp = f.read().strip().splitlines()
  grid = [list(map(int, l)) for l in inp]

  w = len(grid[0])
  h = len(grid)
  seen = (w*2) + ((h-2)*2)
  maxscore = 0

  for y in range(1, h-1):
    for x in range(1, w-1):
      newseen = 0
      score = 1
      for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        newx, newy = x, y
        dirscore = 0
        while True:
          newx += dir[0]
          newy += dir[1]
          if newx < 0 or newx >= w or newy < 0 or newy >= h:
            newseen = 1
            break
          dirscore += 1
          if grid[newy][newx] >= grid[y][x]:
            break
        score *= dirscore
      seen += newseen
      maxscore = max(score, maxscore)

  return seen, maxscore



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]

  inp = setup(filename)

  step1_out = inp[0]
  end_time1 = time.time()

  step2_out = inp[1]
  end_time2 = time.time()

  print(f'Step 1 ({end_time1-start_time:.3f}s): {step1_out}')
  print(f'Step 2 ({end_time2-start_time:.3f}s): {step2_out}\n')


if __name__ == '__main__':
  main()
