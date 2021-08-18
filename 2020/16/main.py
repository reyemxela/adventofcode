#!/bin/env python3

import re
import math

with open('input.txt') as f:
    lines = f.read().split("\n\n")

step1 = 0
step2 = 0

myticket = list(map(int, lines[1].split(":\n")[1].split(",")))
print(myticket)
nearby = lines[2].splitlines()[1:]
numcolumns = len(nearby[0].split(","))

rules = {}
for r in lines[0].splitlines():
    r = r.split(": ")
    rules[r[0]] = list(map(int, filter(None, re.split("(\d+)-(\d+) or (\d+)-(\d+)", r[1]))))
#print(rules)


#rules = [r.split(" ")[-3::2] for r in rules]
#rules = [r for sublist in rules for r in sublist]
#rules = [list(map(int, r.split('-'))) for r in rules]
#rules = '|'.join(F"[{r}]" for r in rules)
#print(rules)



def checkrule(num, r):
    return (num in range(r[0], r[1]+1)) or (num in range(r[2], r[3]+1))
    

valid = []
for i, n in enumerate(nearby):
    isvalid = True
    for pos,num in enumerate(n.split(",")):
        num = int(num)
        for r in rules.items():
            if checkrule(num, r[1]):
                #print(F"{num} in {r[1]}")
                break
        else:
            isvalid = False
            step1 += num
    if isvalid:
        valid.append(i)

numvalid = len(valid)

rulemapping = {}
for r in rules.keys():
    rulemapping[r] = list(range(numcolumns))

print(rulemapping)


columns = [[int(line.split(",")[c]) for line in nearby if nearby.index(line) in valid] for c in range(numcolumns)]
while True:
#for x in range(100):
    for rulename, possible in rulemapping.items():
        if len(possible) == 1:
            for rn, p in rulemapping.items():
                if rn != rulename:
                    if possible[0] in p:
                        p.remove(possible[0])
            continue
        for i,c in enumerate(columns):
            if not all(checkrule(n, rules[rulename]) for n in c):
                if i in possible:
                    possible.remove(i)


#        for r in rules.items():
#                print(F"Removing {i} from {rulemapping[r[0]]}")
#                if i in rulemapping[r[0]]:
#                    rulemapping[r[0]].remove(i)
#        if len(rulemapping[
    if sum(len(i) for i in rulemapping.values()) == len(rulemapping.keys()):
        break

step2 = math.prod(list(myticket[r[1][0]] for r in rulemapping.items() if r[0].startswith("departure")))


#for pos in range(len(nearby[0].split(","))):
#    possible = {}
#    
#    for v in valid:
#        num = int(nearby[v].split(",")[pos])
#        for r in rules.items():
#            if checkrule(num, r[1]):
#                print(F"{num} in {r[1]}")
#                possible[r[0]] = possible.get(r[0], 0) + 1
#            else:
#                print(F"{num} not in {r[1]}")
#    for name, p in possible.items():
#        if p == numvalid:
#            print("yes")
#            order.append(name)
#            break
#    print(possible)


#for v in valid:
#    print(nearby[v])
#    for pos,num in enumerate(nearby[v].split(",")):
#        possible = 0
#        num = int(num)
#        for r in rules.items():
#            print(r[0])
#            if checkrule(num, r[1]):
#                print(F"{num} in {r}")
#                possible += 1
#            else:
#                print(F"{num} not in {r}")
#        print(possible)
#        if possible > 1:
#            print("too many, breaking")
#            break
#        else:
#            print("only one")
#            if r[0] not in order:
#                order.append(r[0])




print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
