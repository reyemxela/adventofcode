from functools import cache


def part1(inp):
  splits = 0
  beams = {inp[0].find('S')}
  for line in inp[1:]:
    splitters = {i for i in range(len(line)) if line[i] == '^'}
    found = beams.intersection(splitters)
    splits += len(found)
    beams.difference_update(found)
    beams |= {i-1 for i in found} | {i+1 for i in found}
  print(splits)


def part2(inp):
  beam = inp[0].find('S')

  @cache
  def split(line, beam):
    if line == len(inp):
      return 1
    if inp[line][beam] == '^':
      return split(line+1, beam-1) + split(line+1, beam+1)
    return split(line+1, beam)
  
  print(split(1, beam))

  pass


with open('input.txt') as f:
  inp = f.read().splitlines()


part1(inp)
part2(inp)
print('------------')