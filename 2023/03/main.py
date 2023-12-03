import re


def part1(input):
  lines = input.splitlines()
  total = 0
  for i in range(len(lines)):
    for match in re.finditer('\d+', lines[i]):
      found = False
      for y in range(i-1, i+2):
        if y < 0 or y >= len(lines):
          continue
        for x in range(match.start()-1, match.end()+1):
          if x < 0 or x >= len(lines[y]):
            continue
          if y == i and (x >= match.start() and x < match.end()): # ignore current match
            continue
          char = lines[y][x]
          if char != '.' and not char.isnumeric():
            found = True
            break # break out of x
        if found:
          break # break out of y
      if found:
        total += int(match.group(0))
  print(total)


def part2(input):
  lines = input.splitlines()
  total = 0
  gears = {}
  for i in range(len(lines)):
    for match in re.finditer('\d+', lines[i]):
      found = False
      for y in range(i-1, i+2):
        if y < 0 or y >= len(lines):
          continue
        for x in range(match.start()-1, match.end()+1):
          if x < 0 or x >= len(lines[y]):
            continue
          if y == i and (x >= match.start() and x < match.end()): # ignore current match
            continue
          char = lines[y][x]
          if char == '*':
            gears.setdefault((x,y), [])
            gears[(x,y)].append(int(match.group(0)))
            found = True
            break # break out of x
        if found:
          break # break out of y
  for numbers in gears.values():
    if len(numbers) == 2:
      total += numbers[0] * numbers[1]
  print(total)


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)