import re


def part1(input):
  input = input.split('\n\n')
  workflows = {}
  for line in input[0].splitlines():
    name, rules = line.split('{')
    rules = rules.strip('}').split(',')
    workflows[name] = rules

  parts = []
  for line in input[1].splitlines():
    part = {}
    for match in re.findall(r'([xmas])=(\d+)', line):
      part[match[0]] = int(match[1])
    parts.append(part)
  
  accepted = 0
  for part in parts:
    x = part['x']
    m = part['m']
    a = part['a']
    s = part['s']
    rules = workflows['in']
    while True:
      for rule in rules[:-1]:
        cond,dest = rule.split(':')
        if eval(cond):
          break
      else:
        dest = rules[-1]

      if dest == 'A':
        accepted += x + m + a + s
        break
      elif dest == 'R':
        break
      else:
        rules = workflows[dest]
  print(accepted)


def part2(input):
  pass


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)