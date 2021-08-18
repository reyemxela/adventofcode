#!/bin/env python3

import hashlib

with open('input.txt') as f:
    lines = f.read().strip()

step1 = 0
step2 = 0

def findresult(num):
    i = 0
    while True:
        result = hashlib.md5((lines + str(i)).encode()).hexdigest()
        if result[:num] == "0"*num:
            break
        i += 1
    return i

step1 = findresult(5)
step2 = findresult(6)


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
