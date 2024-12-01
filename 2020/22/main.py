#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().strip().split("\n\n")

step1 = 0
step2 = 0

player1 = list(map(int, lines[0].split("\n")[1:]))
player2 = list(map(int, lines[1].split("\n")[1:]))

print(player1, player2)

while True:
    p1 = player1.pop(0)
    p2 = player2.pop(0)

    if p1 > p2:
        player1.extend([p1, p2])
    else:
        player2.extend([p2, p1])
    print(player1, player2)
    if not (player1 and player2):
        break

def score(cards):
    return sum(card*(i+1) for i, card in enumerate(cards[::-1]))

step2 = score(player1 if player1 else player2)


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
