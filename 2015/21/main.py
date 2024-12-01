#!/bin/env python3

import sys

DEBUG = False

def readfile(filename):
  with open(filename) as f:
    inp = f.read()
  return inp

def debug(msg=''):
  if DEBUG:
    print(msg)

weapons = {
  'Dagger':     [  8, 4, 0],
  'Shortsword': [ 10, 5, 0],
  'Warhammer':  [ 25, 6, 0],
  'Longsword':  [ 40, 7, 0],
  'Greataxe':   [ 74, 8, 0],
}

armor = {
  'None':       [  0, 0, 0],
  'Leather':    [ 13, 0, 1],
  'Chainmail':  [ 31, 0, 2],
  'Splintmail': [ 53, 0, 3],
  'Bandedmail': [ 75, 0, 4],
  'Platemail':  [102, 0, 5],
}

rings = {
  'None':       [  0, 0, 0],
  'Damage +1':  [ 25, 1, 0],
  'Damage +2':  [ 50, 2, 0],
  'Damage +3':  [100, 3, 0],
  'Defense +1': [ 20, 0, 1],
  'Defense +2': [ 40, 0, 2],
  'Defense +3': [ 80, 0, 3],
}

class Unit:
  def __init__(self, n, h, d, a):
    self.name = n
    self.orighp = self.hp = h
    self.origdmg = self.dmg = d
    self.origarmor = self.armor = a

  def __repr__(self):
    return f'{self.name} - HP: {self.hp} - Damage: {self.dmg} - Armor: {self.armor}'

  def attack(self, other):
    damage = max(1, self.dmg - other.armor)
    other.hp -= damage
    debug(f'{self.name} attacking {other.name} for {damage} total damage')
    debug(f'{self}\n{other}\n')

  def add_equipment(self, eq):
    self.dmg += eq[1]
    self.armor += eq[2]

  def reset(self):
    self.hp = self.orighp
    self.dmg = self.origdmg
    self.armor = self.origarmor
  

def step1(inp):
  player = Unit('Player', 100, 0, 0)
  boss = Unit('Boss', *[int(l.split(': ')[1]) for l in inp.splitlines()])

  debug(player)
  debug(boss)

  lowest_gold = 9999
  highest_gold = 0

  for w in weapons.values():
    for a in armor.values():
      for r1 in rings.values():
        for r2 in rings.values():
          if r1 and r2 and r1 == r2:
            continue
          player.reset()
          boss.reset()
          
          gold = w[0] + a[0] + r1[0] + r2[0]

          player.add_equipment(w)
          player.add_equipment(a)
          player.add_equipment(r1)
          player.add_equipment(r2)

          if play_game(player, boss):
            if gold < lowest_gold:
              lowest_gold = gold
          else:
            if gold > highest_gold:
              highest_gold = gold
  return lowest_gold, highest_gold


def play_game(player, boss):
  rnd = 1
  while True:
    debug(f'Round {rnd}:')
    player.attack(boss)
    if boss.hp <= 0:
      return True
    boss.attack(player)
    if player.hp <= 0:
      return False
    debug()
    rnd += 1


def main():
  filename = "input.txt"

  if len(sys.argv) > 1:
    filename = sys.argv[1]
  inp = readfile(filename)

  step1_out, step2_out = step1(inp)

  print(f'Step 1: {step1_out}')
  print(f'Step 2: {step2_out}')


if __name__ == '__main__':
  main()
