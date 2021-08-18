#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

directions = ['N', 'E', 'S', 'W']
direction = 1
movement = [0, 0, 0, 0]

waypoint = [1, 10, 0, 0]

for l in lines:
    command = l[0]
    value = int(l[1:])

    if command in directions:
        movement[directions.index(command)] += value
    elif command == 'F':
        movement[direction] += value
    elif command in ['L', 'R']:
        value = int(value / 90) #% 4
        direction += value if command == 'R' else -value
        direction = direction % 4
    #print(F"{l} - {movement}")

step1 = abs(movement[0] - movement[2]) + abs(movement[1] - movement[3])
movement = [0, 0, 0, 0]

for l in lines:
    command = l[0]
    value = int(l[1:])

    if command in directions:
        waypoint[directions.index(command)] += value
    elif command == 'F':
        for i in range(4):
            movement[i] += waypoint[i] * value
    elif command in ['L', 'R']:
        value = int(value / 90) % 4
        if command == 'L': value = 4 - value
        for i in range(value):
            waypoint.insert(0, waypoint.pop())
    #print(F"{l} - {movement}")

step2 = abs(movement[0] - movement[2]) + abs(movement[1] - movement[3])

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
