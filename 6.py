#!/usr/bin/python3

import copy

def load_data():
    with open('6.txt') as file:
        input = file.readline()
        input = [int(line.rstrip()) for line in input.split(',')]
        return {n:input.count(n) for n in range(9)}

def run(data, i):
    print(i)
    new_data = []
    for fish in data:
        if fish == 0:
            new_data.append(6)
            new_data.append(8)
        else:
            new_data.append(fish - 1)
    return new_data

def run2(data):
    spawning = copy.deepcopy(data[0])
    for o in range(8):
        data[o] = data[o + 1]
        data[o + 1] = 0
    data[6] += spawning
    data[8] += spawning

data = load_data()
for x in range(256):
    run2(data)
total = 0
for n in data:
    total += data[n]
print("total: ", total)