def part1(inp):
  rangelines = inp[0].splitlines()
  ingredients = list(map(int, inp[1].splitlines()))

  ranges = []
  total = 0

  for r in rangelines:
    b,e = r.split('-')
    b = int(b)
    e = int(e)
    ranges.append(range(b, e+1))

  for ingredient in ingredients:
    if any(ingredient in r for r in ranges):
      total += 1
  print(total)


def part2(inp):
  rangelines = inp[0].splitlines()
  total = 0
  ranges = []
  for r in rangelines:
    b,e = r.split('-')
    b = int(b)
    e = int(e)
    ranges.append({'b': b, 'e': e})

  ranges = sorted(ranges, key=lambda r: (r['b'],r['e']))
  newranges = []

  i = 0
  while i < len(ranges):
    b = ranges[i]['b']
    e = ranges[i]['e']
    i += 1
    while i < len(ranges) and e >= ranges[i]['b']:
      e = max(e,ranges[i]['e'])
      i += 1
    newranges.append({'b': b, 'e': e})

  for r in newranges:
    diff = (r['e']+1 - r['b'])
    total += diff
  print(total)


with open('input.txt') as f:
  inp = f.read().split('\n\n')


part1(inp)
part2(inp)
print('------------')
