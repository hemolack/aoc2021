#!/usr/bin/python3

def load_data():
    with open('7.txt') as file:
        input = file.readline()
        input = [int(line.rstrip()) for line in input.split(',')]
    return input

def fuel_cost(input, target):
    cost = 0
    for p in input:
        print(f'{target} of {len(input)}')
        cost += cost_for_move(abs(target - p))
    return cost

def cost_for_move(distance):
    cost = 0
    c = 1
    for n in range(distance):
        cost += c
        c += 1
    return cost

input = load_data()
print(input)
cost = []
for n in range(min(input), max(input)):
    cost.append(fuel_cost(input, n))
print(f'Postion {cost.index(min(cost))} has minimum cost of {min(cost)}')
