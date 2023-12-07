
def part1(input):
  times, dists = input.splitlines()
  times = list(map(int, times.split(':')[1].split()))
  dists = list(map(int, dists.split(':')[1].split()))

  total = 1
  for race in range(len(times)):
    time = times[race]
    dist = dists[race]
    wins = 0
    for i in range(1, time):
      if (i * (time-i)) > dist:
        wins += 1
    total *= wins
  print(total)


# since I haven't figured out any "easy math trick" for this one,
# I'm doing a binary search to find the beginning of the wins
def part2(input):
  time, dist = input.splitlines()
  time = int(time.split(':')[1].replace(' ', ''))
  dist = int(dist.split(':')[1].replace(' ', ''))

  start = 0
  end = time//2
  pos = 0
  lowest = 0
  while start <= end:
    pos = (start + end) // 2
    res = (pos * (time-pos))
    if res > dist:
      end = pos-1
      lowest = pos
    else:
      start = pos+1
  print(time - (lowest*2) + 1)


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)