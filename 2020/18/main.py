#!/bin/env python3

import re

with open('input.txt') as f:
    lines = f.read().splitlines()

step1 = 0
step2 = 0

def compute(s, rev=False):
    if rev:
        while s.count(" ") > 2:
            ssplit = re.split("(\d+ \+ \d+)", s, 1)
            if len(ssplit) > 1:
                s = ssplit[0] + str(eval(ssplit[1])) + ssplit[2]
            else:
                s = str(eval(s))
    else:
        while s.count(" ") > 2:
            ssplit = s.split(" ", 3)
            s = str(eval(''.join(ssplit[:3]))) + " " + ssplit[3]
            #print(s)
    return eval(s)
    


for l in lines:
    while True:
        #print(''.join(str(i//10) for i in range(len(l))))
        #print(''.join(str(i%10) for i in range(len(l))))
        #print(l)
        depth = 0
        groups = []
        stack = []
        for i, c in enumerate(l):
            if c == "(":
                depth += 1
                stack.append(i)
            elif c == ")" and stack:
                start = stack.pop()
                groups.append((depth, start, i))
                depth -= 1
        if groups:
            groups.sort(reverse=True)
            #print(groups)
            start = groups[0][1]
            end = groups[0][2]
            l = l[:start] + str(compute(l[start+1:end])) + l[end+1:]
        else:
            break
    step1 += compute(l)


for l in lines:
    while True:
        #print(''.join(str(i//10) for i in range(len(l))))
        #print(''.join(str(i%10) for i in range(len(l))))
        #print(l)
        depth = 0
        groups = []
        stack = []
        for i, c in enumerate(l):
            if c == "(":
                depth += 1
                stack.append(i)
            elif c == ")" and stack:
                start = stack.pop()
                groups.append((depth, start, i))
                depth -= 1
        if groups:
            groups.sort(reverse=True)
            #print(groups)
            start = groups[0][1]
            end = groups[0][2]
            l = l[:start] + str(compute(l[start+1:end], True)) + l[end+1:]
        else:
            break
    step2 += compute(l, True)

            




print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
