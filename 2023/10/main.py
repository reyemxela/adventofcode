
directions = {
  '|': set(((0, -1), (0, 1))),
  '-': set(((-1, 0), (1, 0))),
  'L': set(((0, -1), (1, 0))),
  'J': set(((0, -1), (-1, 0))),
  '7': set(((-1, 0), (0, 1))),
  'F': set(((1, 0),  (0, 1))),

}

def part1(input):
  grid = input.splitlines()
  x = 0
  y = 0
  for i in range(len(grid)):
    if 'S' in grid[i]:
      y = i
      x = grid[i].index('S')
      break

  for pos in ((0, -1), (0, 1), (-1, 0), (1, 0)):
    newx = x + pos[0]
    newy = y + pos[1]
    prevdir = (x - newx, y - newy)
    if grid[newy][newx] in directions:
      if prevdir in directions[grid[newy][newx]]:
        x = newx
        y = newy
        break

  steps = 1
  while True:
    if grid[y][x] == 'S':
      break
    newx, newy = directions[grid[y][x]].difference(set((prevdir,))).pop()
    prevdir = (-newx, -newy)
    x += newx
    y += newy
    steps += 1
  print(steps//2)


def part2(input):
  pass


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)