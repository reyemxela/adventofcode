#!/bin/env python3

with open('input.txt') as f:
    lines = list(map(int, f.read().strip().split(',')))


step1 = 0
step2 = 0


def findnum(end):
    lastseen = {}
    for i, n in enumerate(lines[:-1]):
        lastseen[n] = i

    nextnum = lines[-1]

    for i in range(len(lines)-1, end-1):
        if lastseen.get(nextnum) == None:
            lastseen[nextnum] = i
            nextnum = 0
        else:
            diff = i - lastseen[nextnum]
            lastseen[nextnum] = i
            nextnum = diff
    return nextnum

step1 = findnum(2020)
step2 = findnum(30000000)


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
