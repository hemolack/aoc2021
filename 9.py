#!/usr/bin/python

def load_data():
    map = []
    with open('9.txt') as file:
        data = file.readlines()
        for line in data:
            row = [int(char) for char in line.strip()]
            map.append(row)
    return map

def print_map(map):
    for row in map:
        for col in row:
            print(col, end=' ')
        print('')

def risk_map(map):
    riskmap = [[0] * len(map[0]) for _ in range(len(map))]
    for row in range(len(map)):
        for col in range(len(map[0])):
            lowpoint = True
            value = map[row][col]
            if row - 1 >= 0:
                lowpoint = lowpoint and map[row - 1][col] > value
            if col - 1 >= 0:
                lowpoint = lowpoint and map[row][col - 1] > value
            if row + 1 < len(map):
                lowpoint = lowpoint and map[row + 1][col] > value
            if col + 1 < len(map[0]):
                lowpoint = lowpoint and map[row][col + 1] > value
            if lowpoint:
                riskmap[row][col] = 1 + value
            else:
                riskmap[row][col] = 0
    return riskmap

def basin_map(map):
    basinmap = [[0] * len(map[0]) for _ in range(len(map))]
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] < 9:
                basinmap[row][col] = 1
    return basinmap

def mark(row, col, map, bm, label):
    if map[row][col] == 1 and bm[row][col] == 0:
        bm[row][col] = label
        if row - 1 >= 0 and map[row - 1][col] == 1:
            mark(row - 1, col, map, bm, bm[row][col])
        if col - 1 >= 0 and map[row][col] == 1:
            mark(row, col - 1, map, bm, bm[row][col])
        if row + 1 < len(map) and map[row + 1][col] == 1:
            mark(row + 1, col, map, bm, bm[row][col])
        if col + 1 < len(map[0]) and map[row][col] == 1:
            mark(row, col + 1, map, bm, bm[row][col])
    else:
        return

def count_basins(map):
    bm = [[0] * len(map[0]) for _ in range(len(map))]
    label = 1
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 1:
                mark(row, col, map, bm, label)
                label += 1
    flat_list = [col for row in bm for col in row if col > 0]
    counts = {}
    for value in flat_list:
        if value in counts.keys():
            counts[value] += 1
        else:
            counts[value] = 1
    big_basins = sorted(counts.values(), reverse=True)
    print(f'Answer: {big_basins[0] * big_basins[1] * big_basins[2]}')
    return bm

def evaluate_risk(map):
    print(sum(sum(map, [])))

map = load_data()
riskmap = risk_map(map)
evaluate_risk(riskmap)
basin_map = basin_map(map)
count_basins(basin_map)
