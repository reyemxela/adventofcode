#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0


def process_lines(l):
    line = 0
    seen = []
    acc = 0
    target = len(l)
    while True:
        if line in seen:
            return False, acc
        elif line > target:
            return False, None
        elif line == target:
            return True, acc

        seen.append(line)

        inst, val = l[line].split()
        val = int(val)
        
        if inst == "jmp":
            line += val
        else:
            if inst == "acc":
                acc += val
            line += 1



_,step1 = process_lines(lines)


for i in range(len(lines)):
    newlines = lines.copy()
    if newlines[i].startswith("nop"):
        newlines[i] = newlines[i].replace("nop", "jmp")
    elif newlines[i].startswith("jmp"):
        newlines[i] = newlines[i].replace("jmp", "nop")
    else:
        continue
    exited, step2 = process_lines(newlines)
    if exited == True:
        break


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
