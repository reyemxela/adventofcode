
def part1(input):
  total1 = 0
  total2 = 0
  for line in input.splitlines():
    diffs = [list(map(int, line.split()))]
    while True:
      diffs.append([])
      prevnum = diffs[-2][0]
      for num in diffs[-2][1:]:
        diffs[-1].append(num - prevnum)
        prevnum = num
      if all(x == 0 for x in diffs[-1]):
        break
    diffs[-1].append(0)
    for i in range(len(diffs)-2, -1, -1):
      diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
      diffs[i].insert(0, diffs[i][0] - diffs[i+1][0])
    total1 += diffs[0][-1]
    total2 += diffs[0][0]
  print(total1)
  print(total2)


with open('input.txt') as f:
  inp = f.read()


part1(inp)