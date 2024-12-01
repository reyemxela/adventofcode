#!/bin/env python3

import sys
import time
import shutil

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

DEBUG = False

def debug(s=''):
  if DEBUG:
    print(s)


# had some fun with this one, implementing dijkstra pathfinding and
# doing some fun visualizations

# 0 = braille, 1 = numbers from input
mode = 0


maxw, maxh = shutil.get_terminal_size()

def step1(inp):
  print('\033[2J')
  grid = {}
  height = len(inp)
  width = len(inp[0])
  for y, line in enumerate(inp):
    for x, dist in enumerate(line):
      grid[(x, y)] = int(dist)
  debug(grid)
  debug(f'{width=} {height=}')

  return dijkstra(grid, (0,0), (width-1,height-1), width, height)



def step2(inp):
  time.sleep(1)
  print('\033[2J')

  grid = {}
  height = len(inp)
  width = len(inp[0])
  for y, line in enumerate(inp):
    for x, dist in enumerate(line):
      for y2 in range(0, 5):
        for x2 in range(0, 5):
          grid[(x+x2*width, y+y2*height)] = (int(dist) + x2 + y2 - 1) % 9 + 1
  debug(grid)
  width = width*5
  height = height*5

  return dijkstra(grid, (0,0), (width-1,height-1), width, height)


def dijkstra(grid, start, end, width, height):
  dist = {}
  parent = {}

  for node in grid:
    dist[node] = sys.maxsize
    parent[node] = None
  dist[start] = 0

  unexplored = set(grid.keys())
  potentials = set()

  prev_time = time.time() - 1
  node = None
  while unexplored:
    if node == None:
      node = start
    else:
      node = sorted(potentials, key=lambda x: dist[x])[0]

    potentials.discard(node)
    unexplored.discard(node)
    x, y = node

    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
      new_node = (x+dx, y+dy)
      if not new_node in unexplored:
        continue
      new_dist = dist[node] + grid[new_node]
      if new_dist < dist[new_node]:
        dist[new_node] = new_dist
        parent[new_node] = node
      potentials.add(new_node)

    t = time.time()
    if t - prev_time > .1:
      print_grid(grid, width, height, unexplored, node, new_node, start, end)
      prev_time = t
  print_grid(grid, width, height, unexplored, node, new_node, start, end)

  return dist[end]


b = ' ⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿'
def print_grid(grid, width, height, unexplored, node, new_node, start, end):
  print('\033[H')

  skip = max(1, min(width // maxw + 1, height // maxh + 1))

  if mode == 0:
    w = min(width, (maxw - 5) * 2 * skip)
    h = min(height, (maxh - 7) * 3 * skip)

    for y in range(0, h, 3*skip):
      for x in range(0, w, 2*skip):
        cx, cy = width-w+x, height-h+y
        c = b[int(''.join(str(int(cx+dx < width and cy+dy < height and not (cx+dx,cy+dy) in unexplored)) for dx in range(1, -1, -1) for dy in range(2, -1, -1)), 2)]
        print(c, end='')
      print()

  else:
    w = min(width, maxw - 5)
    h = min(height, maxh - 7)

    for y in range(0, h):
      for x in range(0, w):
        color = ''
        cur_node = (width-w+x, height-h+y)
        if cur_node == node:
          color = '\033[42m'
        elif cur_node == new_node:
          color = '\033[33m'
        elif not cur_node in unexplored:
          color = '\033[32m'
        print(f'{color}{grid[cur_node]}\033[0m', end='')
      print()
  print(f'\n\033[K{node=} {new_node=} {skip=}', end='')



def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename).splitlines()

  step1_out = step1(inp)
  step2_out = step2(inp)

  print(f'\nStep 1: {step1_out}')
  print(f'Step 2: {step2_out}')
  input()


if __name__ == '__main__':
  main()
