#!/usr/bin/python3

last = -1
increases = 0
with open('1.txt') as file:
    input = file.readlines()
    input = [int(line.rstrip()) for line in input]
for idx, i in enumerate(input):
    if idx > len(input) - 3:
        break
    val = input[idx] + input[idx + 1] + input[idx + 2]
    if last > -1 and val > last:
        increases += 1
    last = val
print(increases)