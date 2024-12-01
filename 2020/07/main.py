#!/bin/env python3

import re

with open('input.txt') as f:
    lines = f.read()

rules = {}
rules2 = {}

#for l in lines.splitlines()[530:532]:
for l in lines.splitlines():
    rule = re.findall("([0-9]?) ?(\w+ \w+) bags?", l)
    outer = rule[0][1]
    inner = rule[1:]
    for i in inner:
        rules.setdefault(i[1], []).append(outer)
        rules2.setdefault(outer, []).append(i)


def find_outer(color):
    seen = []
    for outer in rules[color]:
        seen.append(outer)
        if rules.get(outer):
            for r in find_outer(outer):
                if r not in seen:
                    seen.append(r)
    return seen

def find_inner(color, depth=0):
    num = 0
    for inner in rules2[color]:
        if inner[1] != 'no other':
            if rules2.get(inner[1]):
                num += int(inner[0]) * find_inner(inner[1], depth+1)
    return min(1,depth)+num

print(F"Step 1: {len(find_outer('shiny gold'))}")
print(F"Step 2: {find_inner('shiny gold')}")
