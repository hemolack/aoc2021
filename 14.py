#!/usr/bin/python

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

for step in range(10):
    print('step', step, counts)
    newpairs = {}
    for pair in pairs.keys():
        newpairs[pair] = pairs[pair]
        for _ in range(pairs[pair]):
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            newpairs[pair] -= 1
            if new_pair_1 in newpairs.keys():
                newpairs[new_pair_1] += 1
            else:
                newpairs[new_pair_1] = 1
            if new_pair_2 in newpairs.keys():
                newpairs[new_pair_2] += 1
            else:
                newpairs[new_pair_2] = 1
            if rules[pair] in counts.keys():
                counts[rules[pair]] += 1
            else:
                counts[rules[pair]] = 1
    pairs = newpairs

print(counts)
answer = max(counts.values()) - min(counts.values())
print(answer)

# for step in range(10):
#     print('Step', step)
#     replacements = []
#     for i in range(len(polymer) - 1):
#         pair = polymer[i : (i + 2)]
#         if i == 0:
#             replacements.append(f'{pair[0]}{rules[pair]}{pair[1]}')
#         else:
#             replacements.append(f'{rules[pair]}{pair[1]}')
#     polymer = ''.join(replacements)

# elements = list(set(polymer))
# counts = {}
# for e in elements:
#     counts[e] = polymer.count(e)

# print(counts)
# answer = max(counts.values()) - min(counts.values())
# print(answer)
