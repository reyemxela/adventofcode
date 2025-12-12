def part1(inp):
  pos = 50
  total = 0
  for line in inp:
    dir = line[0]
    num = int(line[1:])
    if dir == 'R':
      pos += num
    else:
      pos -= num
    pos %= 100

    if pos == 0:
      total += 1
  print(total)


def part2(inp):
  pos = 50
  total = 0
  for line in inp:
    dir = line[0]
    num = int(line[1:])
    step = 1 if dir == 'R' else -1

    # this is a dumb way to do it, but trying to do divmod/etc is giving me trouble at the moment
    for _ in range(0, num):
      pos += step
      pos %= 100
      if pos == 0:
        total += 1
  print(total)


with open('input.txt') as f:
  inp = f.read().splitlines()


part1(inp)
part2(inp)
print('------------')