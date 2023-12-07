
def part1(input):
  card_map = str.maketrans('TJQKA', 'ABCDE') # make cards sortable by value
  hand_strengths = {}
  for line in input.splitlines():
    cards, bid = line.split()
    cards = cards.translate(card_map)
    hand = {'cards': cards, 'bid': bid}

    counts = list({c:cards.count(c) for c in cards}.values())
    strength = 0
    if 5 in counts: # five of a kind
      strength = 6
    elif 4 in counts: # 4 of a kind
      strength = 5
    elif 3 in counts and 2 in counts: # full house (3+2)
      strength = 4
    elif 3 in counts: # 3 of a kind
      strength = 3
    elif counts.count(2) == 2: # 2 pair
      strength = 2
    elif 2 in counts: # 1 pair
      strength = 1
    else: # high card
      strength = 0
    hand_strengths.setdefault(strength, []).append(hand)

  total = 0
  rank = 1
  for strengths in sorted(hand_strengths.items(), key=lambda x: x[0]):
    for hand in sorted(strengths[1], key=lambda x: x['cards']):
      total += int(hand['bid']) * rank
      rank += 1
  print(total)


def part2(input):
  card_map = str.maketrans('TJQKA', 'A1BCD') # make cards sortable by value, jokers are 1
  hand_strengths = {}
  for line in input.splitlines():
    cards, bid = line.split()
    cards = cards.translate(card_map)
    hand = {'cards': cards, 'bid': bid}

    counts = sorted(list({c:cards.count(c) for c in cards if c != '1'}.values()), reverse=True) # get all counts except jokers (1)
    jokers = cards.count('1')
    first = counts[0] if counts else 0
    second = counts[1] if len(counts) > 1 else 0

    strength = 0
    if first + jokers == 5: # five of a kind
      strength = 6
    elif first + jokers == 4: # 4 of a kind
      strength = 5
    elif len(counts) >= 2 and (first + second + jokers == 5): # full house (3+2)
      strength = 4
    elif first + jokers == 3: # 3 of a kind
      strength = 3
    elif len(counts) >= 2 and (first + second + jokers == 4): # 2 pair
      strength = 2
    elif first + jokers == 2: # 1 pair
      strength = 1
    else: # high card
      strength = 0
    hand_strengths.setdefault(strength, []).append(hand)

  total = 0
  rank = 1
  for strengths in sorted(hand_strengths.items(), key=lambda x: x[0]):
    for hand in sorted(strengths[1], key=lambda x: x['cards']):
      total += int(hand['bid']) * rank
      rank += 1
  print(total)


with open('input.txt') as f:
  inp = f.read()


part1(inp)
part2(inp)