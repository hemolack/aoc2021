#!/usr/bin/python

from math import ceil

polymer = ''
rules = {}
pairs = {}
counts = {}

with open('14.txt') as file:
    i = 0
    for line in file.readlines():
        if i == 0:
            polymer = line.strip()
        elif len(line.strip()) > 0:
            part = line.strip().split(' -> ')
            rules[part[0]] = part[1]
            pairs[part[0]] = 0
        i += 1

for i in range(len(polymer) - 1):
    pair = polymer[i : (i + 2)]
    pairs[pair] += 1

for i in range(len(polymer)):
    if polymer[i] in counts.keys():
        counts[polymer[i]] += 1
    else:
        counts[polymer[i]] = 1

for step in range(40):
    newpairs = {}
    for pair, value in pairs.items():
        new_pair_1 = pair[0] + rules[pair]
        new_pair_2 = rules[pair] + pair[1]
        newpairs[new_pair_1] = newpairs.setdefault(new_pair_1, 0) + value
        newpairs[new_pair_2] = newpairs.setdefault(new_pair_2, 0) + value
    pairs = newpairs

counts = {}
for pair, value in pairs.items():
    counts[pair[0]] = counts.setdefault(pair[0], 0) + value
    counts[pair[1]] = counts.setdefault(pair[1], 0) + value
counts = sorted([ceil(val / 2) for val in counts.values()])
answer = max(counts) - min(counts)
print(answer)
