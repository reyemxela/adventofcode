import re

def part1(input):
  directions, node_lines = input.split('\n\n')
  nodes = {}
  for line in node_lines.splitlines():
    key, l, r = re.findall('[A-Z]+', line)
    nodes[key] = {'L': l, 'R': r}

  current = 'AAA'
  index = 0
  total = 0
  while current != 'ZZZ':
    dir = directions[index]
    current = nodes[current][dir]

    index = (index + 1) % len(directions)
    total += 1
  print(total)


def part2(input):
  pass

with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)