#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

preamble = 25

def check_before():
    for l in range(preamble, len(lines)):
        completed = False
        #print(F"{l} {lines[l]} - {lines[l-preamble:l]}")
        for i in range(l-preamble, l-1):
            for j in range(i+1, l):
                if int(lines[i])+int(lines[j]) == int(lines[l]):
                    #print(F"{lines[i]}+{lines[j]} = {int(lines[l])}")
                    completed = True
                if completed: break
            if completed: break
        if not completed: return int(lines[l])

step1 = check_before()

def find_series(target):
    for start in range(0, len(lines)-2):
        for end in range(start+2, len(lines)):
            block = list(map(int, lines[start:end]))
            total = sum(block)
            if total > target: break
            if total == target:
                block.sort()
                print(block)
                return block[0] + block[-1]

step2 = find_series(step1)

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
