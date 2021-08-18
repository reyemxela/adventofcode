#!/bin/env python3

import re

with open('input.txt') as f:
    lines = f.read().split("\n\n")

step1 = 0
step2 = 0

rules = {}

messages = lines[1].splitlines()

for l in lines[0].splitlines():
    num, rule = l.split(": ")
    rule = rule.replace('"', '')
    rules[num] = rule


def replace(match):
    rule = rules[match.group()]
    if rule not in ['a', 'b']:
        rule = F"({rule})"
    return rule

r0 = rules['0']
while True:
    if re.search("\d+", r0):
        r0 = re.sub("\d+", replace, r0)
    else:
        break

r0 = r0.replace(' ', '')

for m in messages:
    if re.match(F"^{r0}$", m):
        step1 += 1

rules['8'] += ' | (42)+'
rules['11'] += ' | 42 11 31'
r0 = rules['0']

i = 0
while True:
    if re.search("\d+", r0):
        if i == 4: # lol
            rules['11'] = '42 31'
        r0 = re.sub("\d+", replace, r0)
    else:
        break
    i += 1

r0 = r0.replace(' ', '')

for m in messages:
    if re.match(F"^{r0}$", m):
        step2 += 1



print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
