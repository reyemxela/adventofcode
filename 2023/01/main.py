import time
import sys
from signal import signal, SIGINT

def part1(input):
  total = 0
  for line in input.splitlines():
    numbers = []
    for c in line:
      if c.isnumeric():
        numbers.append(c)
    result = int(numbers[0] + numbers[-1])
    total += result
  print(total)

number_map = {
  'one': '1', 'two': '2', 'three': '3',
  'four': '4', 'five': '5', 'six': '6',
  'seven': '7', 'eight': '8', 'nine': '9'
}

def part2(input):
  total = 0
  for line in input.splitlines():
    numbers = []
    for i in range(len(line)):
      if line[i].isnumeric():
        numbers.append(line[i])
      else:
        for num in number_map.keys():
          if line[i:].startswith(num):
            numbers.append(number_map[num])
            break
    result = int(numbers[0] + numbers[-1])
    total += result
  print(total)


class esc:
  HOME = '\033[H'
  CLEAR = '\033[2J'
  CLEARLINE = '\033[2K'
  UP = '\033[1A'
  DOWN = '\033[1B'
  HOMELINE = '\033[1000D'
  HIDECURSOR = '\033[?25l'

  RESET = '\033[0m'
  BOLD = '\033[1m'

  BRRED = '\033[91m'
  BRGREEN = '\033[92m'
  def pos(x, y):
    return F"\033[{y+1};{x+1}H"


def print_pt2(line, pos, numbers, found_num, newline):
  numlen = max(len(found_num), 1)
  found = esc.BOLD if found_num else ''
  if not newline:
    sys.stdout.write(f'{esc.UP}{esc.CLEARLINE}{esc.UP}{esc.CLEARLINE}{esc.HOMELINE}')
    sys.stdout.flush()
  print(
    f'{esc.BRRED}' +
    f'{line[:pos]}' +
    f'{esc.RESET}[{esc.BRGREEN}{found}' +
    f'{line[pos:pos+numlen]}' +
    f'{esc.RESET}]{esc.BRGREEN}' +
    f'{line[pos+numlen:]}' +
    f'{esc.RESET}'
  )
  print('numbers: ' + ' '.join(numbers))
  time.sleep(.05)


def part2_vis(input):
  def handler(sig, frame):
    sys.stdout.write(esc.RESET + "\n")
    sys.stdout.flush()
    exit(0)
  signal(SIGINT, handler)

  total = 0
  for line in input.splitlines():
    numbers = []
    newline = True
    for i in range(len(line)):
      found_key = ''
      found_num = ''
      if line[i].isnumeric():
        found_key = line[i]
        found_num = line[i]
      else:
        for num in number_map.keys():
          if line[i:].startswith(num):
            found_key = num
            found_num = number_map[num]
            break
      if found_num:
        numbers.append(found_num)
      print_pt2(line, i, numbers, found_key, newline)
      newline = False
    result = int(numbers[0] + numbers[-1])
    total += result
  print(total)


with open('input.txt') as f:
  inp = f.read()

part1(inp)
part2(inp)
# part2_vis(inp)