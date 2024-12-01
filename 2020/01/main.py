#!/bin/env python3

with open('input.txt') as f:
    lines = [int(line.strip()) for line in f if line.strip()]


def find2(a):
    for i in range(len(a) - 1):
        for j in range(i, len(a)):
            if (a[i] + a[j]) == 2020:
                return a[i] * a[j]


def find3(a):
    for i in range(len(a) - 2):
        for j in range(i, len(a) - 1):
            for k in range(j, len(a)):
                if (a[i] + a[j] + a[k]) == 2020:
                    return a[i] * a[j] * a[k]

print(F"Step 1: {find2(lines)}")
print(F"Step 2: {find3(lines)}")
