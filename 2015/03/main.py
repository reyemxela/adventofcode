#!/bin/env python3

with open('input.txt') as f:
    lines = f.read()

step1 = 0
step2 = 0

visited = ["0.0"]

x = 0
y = 0
x2 = [0, 0]
y2 = [0, 0]
turn = 0

for step in lines.strip():
    if step == '^': y += 1
    if step == '>': x += 1
    if step == 'v': y -= 1
    if step == '<': x -= 1
    key = F"{x}.{y}"

    if key not in visited:
        visited.append(key)

step1 = len(visited)

visited = ["0.0"]

for step in lines.strip():
    if step == '^': y2[turn] += 1
    if step == '>': x2[turn] += 1
    if step == 'v': y2[turn] -= 1
    if step == '<': x2[turn] -= 1
    key = F"{x2[turn]}.{y2[turn]}"

    if key not in visited:
        visited.append(key)
    turn = (turn + 1) % 2

step2 = len(visited)


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
