from copy import deepcopy

ADJACENT = (
  (-1,-1), (0,-1), (1,-1),
  (-1, 0),         (1, 0),
  (-1, 1), (0, 1), (1, 1),
)

def printgrid(grid):
  for y in range(len(grid)):
    print(''.join(grid[y]))


def part1(inp):
  grid = [[x for x in y] for y in inp]
  # printgrid(grid)
  total = 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] != '@':
        continue
      rolls = 0
      for rx,ry in ADJACENT:
        tx = x+rx
        ty = y+ry
        if tx < 0 or tx >= len(grid[y]) or ty < 0 or ty >= len(grid):
          continue
        rolls += int(grid[ty][tx] == '@')
        if rolls >= 4:
          break
      else:
        total += 1
  # printgrid(grid)
  print(total)


def part2(inp):
  grid = [[x for x in y] for y in inp]
  newgrid = deepcopy(grid)
  # printgrid(grid)
  total = 0
  while True:
    done = True
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        if grid[y][x] != '@':
          continue
        rolls = 0
        for rx,ry in ADJACENT:
          tx = x+rx
          ty = y+ry
          if tx < 0 or tx >= len(grid[y]) or ty < 0 or ty >= len(grid):
            continue
          rolls += int(grid[ty][tx] == '@')
          if rolls >= 4:
            break
        else:
          newgrid[y][x] = '.'
          total += 1
          done = False
    grid = newgrid
    # printgrid(grid)
    if done:
      break
    newgrid = deepcopy(grid)
  print(total)


with open('input.txt') as f:
  inp = f.read().splitlines()


part1(inp)
part2(inp)
print('------------')