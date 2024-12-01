#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().strip()

step1 = 0
step2 = 0

cups1 = list(map(int, list(lines)))
cups2 = list(map(int, list(lines))) + list(range(10, 1000001))

nummoves1 = 100
#nummoves2 = 10000000
nummoves2 = 100


def play(nummoves, cups):
    currentlabel = cups[0]
    for i in range(nummoves):
        #print(F"cups: {cups}")
        destlabel = currentlabel - 1
        picked = [cups.pop((cups.index(currentlabel) + 1) % len(cups)) for _ in range(3)]
        while True:
            if destlabel in cups:
                break
            destlabel -= 1
            if destlabel < min(cups):
                destlabel = max(cups)
                break
        destpos = cups.index(destlabel) + 1
        cups[destpos:destpos] = picked
        #print(F"picked up: {picked}\ncurrent: {currentlabel}\ndest: {destlabel}\n")
        currentlabel = cups[(cups.index(currentlabel) + 1) % len(cups)]
    return cups

step1 = play(nummoves1, cups1)
step1 = ''.join(map(str, step1[step1.index(1)+1:] + step1[:step1.index(1)]))

result = play(nummoves2, cups2.copy())
resultindex = result.index(1)
result = [result[(resultindex + 1) % len(result)], result[(resultindex + 2) % len(result)]]
step2 = result[0] * result[1]

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
