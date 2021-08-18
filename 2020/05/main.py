#!/bin/env python3

with open('input.txt') as f:
    lines = f.read().split("\n")

def parse_seat(seat):
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(seat[7:10].replace('L', '0').replace('R', '1'), 2)
    seatid = (row * 8) + col

    return seatid

step1 = 0
step2 = 0

seatids = []

for l in lines:
    if l:
        seatid = parse_seat(l)
        seatids.append(seatid)
        if seatid > step1:
            step1 = seatid

for i in range(1,step1):
    if i not in seatids and i+1 in seatids and i-1 in seatids:
        step2 = i
        break


print(F"Step 1: {step1}")
print(F"Step 2: {step2}")
