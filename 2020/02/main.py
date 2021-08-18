#!/bin/env python3

with open('input.txt') as f:
    lines = f.read()

valid1 = 0
valid2 = 0

for l in lines.split("\n"):
    if l:
        nums, letter, password = l.split(" ")
        num1, num2 = map(int, nums.split("-"))
        letter = letter[0]
        if num1 <= password.count(letter) <= num2:
            valid1 += 1
        if (password[num1 - 1] == letter) ^ (password[num2 - 1] == letter):
            valid2 += 1

print(F"Step 1: {valid1}")
print(F"Step 2: {valid2}")
