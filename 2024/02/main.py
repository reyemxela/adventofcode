def check_level(line):
  safe = True
  if line != sorted(line) and line != sorted(line, reverse=True):
    safe = False
  else:
    for i in range(len(line) - 1):
      diff = abs(line[i] - line[i+1])
      if diff < 1 or diff > 3:
        safe = False
        break
  return safe


def part1(input):
  data = [list(map(int, line.split())) for line in input.splitlines()]
  num_safe = 0
  for line in data:
    if check_level(line):
      num_safe += 1
  print(num_safe)


def part2(input):
  data = [list(map(int, line.split())) for line in input.splitlines()]
  num_safe = 0
  for line in data:
    if check_level(line):
      num_safe += 1
    else:
      for i in range(len(line)):
        if check_level(line[:i] + line[i+1:]):
          num_safe += 1
          break
  print(num_safe)
  pass


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)
print('------------')