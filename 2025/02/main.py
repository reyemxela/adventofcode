def part1(inp):
  invalid = []
  for rnge in inp.split(','):
    start, end = map(int, rnge.split('-'))
    for num in range(start, end+1):
      numstr = str(num)
      numlen = len(numstr)
      if numlen%2 == 1:
        continue
      # if the first half equals the second half:
      if numstr[:numlen//2] == numstr[numlen//2:]:
        invalid.append(num)
  print(sum(invalid))


def part2(inp):
  invalid = []
  for rnge in inp.split(','):
    start, end = map(int, rnge.split('-'))
    for num in range(start, end+1):
      numstr = str(num)
      numlen = len(numstr)
      # from 1 to half the length
      for i in range(1, (numlen//2)+1):
        # first i characters, repeated numlen/i times
        if numstr[:i] * (numlen//i) == numstr:
          invalid.append(num)
          break
  print(sum(invalid))


with open('input.txt') as f:
  inp = f.read().strip()


part1(inp)
part2(inp)
print('------------')