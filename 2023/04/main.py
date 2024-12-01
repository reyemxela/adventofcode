import re


def part1(input):
  total = 0
  for line in input.splitlines():
    line = line.split(':')[1]
    winning, have = line.split('|')
    winning = list(map(int, re.findall('(\d+)', winning)))
    have = list(map(int, re.findall('(\d+)', have)))
    num = len(set(have).intersection(set(winning)))
    if num > 0:
      total += 2**(num-1)
  print(total)


def part2(input):
  cards = {}
  for line in input.splitlines():
    id, line = line.split(':')
    id = int(id.split()[1])
    winning, have = line.split('|')
    winning = list(map(int, re.findall('(\d+)', winning)))
    have = list(map(int, re.findall('(\d+)', have)))
    num = len(set(have).intersection(set(winning)))
    cards.setdefault(id, 1)
    for i in range(1, num+1):
      cards.setdefault(id+i, 1)
      cards[id+i] += cards[id]
  print(sum(cards.values()))


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)