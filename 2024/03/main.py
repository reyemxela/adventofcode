import re


def mul(input):
  total = 0
  for pair in re.findall(r'mul\((\d+),(\d+)\)', input):
    total += int(pair[0]) * int(pair[1])
  return total


def part1(input):
  print(mul(input))


def part2(input):
  print(mul(''.join(re.split(r'don\'t\(\).*?do\(\)', input))))


with open('input.txt') as f:
  inp = f.read().replace('\n','')


part1(inp)
part2(inp)
print('------------')