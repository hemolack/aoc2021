#!/usr/bin/python

import math

opens = [ '(', '[', '{', '<' ]
closes = { '(': ')', '[': ']', '{': '}', '<': '>' }
score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
fix_score = { ')': 1, ']': 2, '}': 3, '>': 4 }

def load_data():
    with open('10.txt') as file:
        data = [line.rstrip() for line in file.readlines()]
    return data

data = load_data()
good = []
total = 0

for line in data:
    stack = []
    error = 0
    for char in line:
        if char in opens:
            stack.append(char)
        elif char in closes.values() and len(stack) > 0:
            o = stack.pop()
            if closes[o] != char:
                error += score[char]
                break
        if len(stack) == 0:
            break
    if error > 0:
        total += error
    else:
        good.append(line)

i = 0
completion_list = []
for line in good:
    i += 1
    stack = []
    complete = 0
    for char in line:
        if char in opens:
            stack.append(char)
        elif char in closes.values() and len(stack) > 0:
            o = stack.pop()
    completion_string = ''
    while len(stack) > 0:
        missing = stack.pop()
        completion_string += closes[missing]
    completion_list.append(completion_string)

score_list = []
for completion in completion_list:
    completion_score = 0
    for char in completion:
        completion_score = (completion_score * 5) + fix_score[char]
    score_list.append(completion_score)

print('Part 1:', total)
print('Part 2:', sorted(score_list)[math.floor(len(score_list) / 2)])