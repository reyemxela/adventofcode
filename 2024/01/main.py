def part1(l1, l2):
  l1.sort()
  l2.sort()
  print(sum(abs(l1[i]-l2[i]) for i in range(len(l1))))


def part2(l1, l2):
  total = 0
  for i in l1:
    total += i * l2.count(i)
  print(total)


with open('input.txt') as f:
  inp = f.read()

inp = inp.split()
l1 = list(map(int, inp[0::2]))
l2 = list(map(int, inp[1::2]))

part1(l1[:], l2[:])
part2(l1[:], l2[:])
print('------------')