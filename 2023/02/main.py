import re


def part1(input):
  MAXRED = 12
  MAXGREEN = 13
  MAXBLUE = 14
  total = 0
  for line in input.splitlines():
    id = int(re.match('Game (\d+)', line).group(1))
    red = list(map(int, re.findall('(\d+) red', line)))
    green = list(map(int, re.findall('(\d+) green', line)))
    blue = list(map(int, re.findall('(\d+) blue', line)))
    if any(r > MAXRED for r in red):
      continue
    elif any(g > MAXGREEN for g in green):
      continue
    elif any(b > MAXBLUE for b in blue):
      continue
    total += id
  print(total)
    

def part2(input):
  total = 0
  for line in input.splitlines():
    red = list(map(int, re.findall('(\d+) red', line)))
    green = list(map(int, re.findall('(\d+) green', line)))
    blue = list(map(int, re.findall('(\d+) blue', line)))
    total += max(red) * max(green) * max(blue)
  print(total)


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)