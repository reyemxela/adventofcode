#!/bin/env python3

import re


with open('input.txt') as f:
    lines = f.read().replace("\n", " ").split("  ")


fields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]
fields2 = [ "byr:(19[2-9][0-9]|200[0-2])",
            "iyr:(20(1[0-9]|20))",
            "eyr:(20(2[0-9]|30))",
            "hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)",
            "hcl:#[0-9a-fA-F]{6}",
            "ecl:(amb|blu|brn|gry|grn|hzl|oth)",
            "pid:[0-9]{9}" ]

step1 = 0
step2 = 0

for passport in lines:
    for f in fields:
        if not passport.count(f):
            break
    else:
        step1 += 1

    for f in fields2:
        match = re.search(F"{f}( |$)", passport)
        if not match:
            break
    else:
        step2 += 1

print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
