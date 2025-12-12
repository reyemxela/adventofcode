import math


def part1(inp):
  problems = [list(map(int, line.split())) for line in inp[:-1]]
  operators = inp[-1].split()
  total = 0
  for i in range(len(problems[0])):
    oper = sum if operators[i] == '+' else math.prod
    total += oper(p[i] for p in problems)
  print(total)


def part2(inp):
  problems = inp[:-1]
  operators = inp[-1]

  problen = len(problems)
  pos = len(problems[0]) - 1
  total = 0
  nums = []

  while pos >= 0:
    num = ''.join(problems[i][pos] for i in range(problen))
    if num.strip():
      nums.append(int(num))

    if operators[pos].strip():
      oper = sum if operators[pos] == '+' else math.prod
      total += oper(nums)
      nums = []

    pos -= 1

  print(total)


with open('input.txt') as f:
  inp = f.read().splitlines()


part1(inp)
part2(inp)
print('------------')