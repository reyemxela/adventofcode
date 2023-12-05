
def part1(input):
  input_sections = input.split('\n\n')
  seeds = list(map(int, input_sections[0].split(':')[1].split()))
  maps = [parse_section(i) for i in input_sections[1:]]

  seed_to_location = {}
  for seed in seeds:
    result = seed
    for m in maps:
      for rng,offset in m.items():
        if result >= rng[0] and result <= rng[1]:
          result = result + offset
          break
    seed_to_location[seed] = result
  print(min(l for l in seed_to_location.values()))


def part2(input):
  pass


def parse_section(input):
  output = {}
  numbers = input.split(':')[1].strip()
  for line in numbers.splitlines():
    dest, src, length = map(int, line.split())
    output[(src, src+length-1)] = dest-src

  return output


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)
