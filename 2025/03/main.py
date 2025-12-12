def part1(inp):
  total = 0
  for line in inp:
    pos1 = line.index(max(line[:-1]))
    pos2 = line.index(max(line[pos1+1:]))
    total += int(line[pos1] + line[pos2])
  print(total)


def part2(inp):
  total = 0
  for line in inp:
    number = ''
    start = 0
    end = len(line)-11
    for _ in range(0, 12):
      search = line[start:end]
      pos = search.index(max(search))
      number += search[pos]
      end += 1
      start += pos+1
    total += int(number)
  print(total)


with open('input.txt') as f:
  inp = f.read().splitlines()


part1(inp)
part2(inp)
print('------------')