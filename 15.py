#!/usr/bin/python

import networkx as nx

graph = nx.DiGraph()

def wrap_value(n):
    if n > 9: return n - 9
    else: return n

def tile_map(map):
    new_map = []
    for j in range(5):
        for row in map:
            new_row = []
            for i in range(5):
                new_row = new_row + [wrap_value(x + i + j) for x in row]
            new_map.append(new_row)
    return new_map

def load_data(graph):
    map = []
    with open('15.txt') as file:
        for line in file.readlines():
            row = []
            for col in [char for char in line.strip()]:
                row.append(int(col))
            map.append(row)
    map = tile_map(map)
    for r, row in enumerate(map):   # Add nodes
        for c, col in enumerate(row):
            graph.add_node(f'{r},{c}')
    for r, row in enumerate(map):   # Add edges
        for c, col in enumerate(row):
            if r + 1 < len(map):
                graph.add_edge(f'{r},{c}', f'{r + 1},{c}', weight = map[r + 1][c])
                graph.add_edge(f'{r + 1},{c}', f'{r},{c}', weight = map[r][c])
            if c + 1 < len(map[0]):
                graph.add_edge(f'{r},{c}', f'{r},{c + 1}', weight = map[r][c + 1])
                graph.add_edge(f'{r},{c + 1}', f'{r},{c}', weight = map[r][c])
    return map

def print_map(map):
    for row in map:
        for col in row:
            print(col, end = '')
        print('')

map = load_data(graph)
cost = nx.dijkstra_path_length(graph, source = '0,0', target = f'{len(map) - 1},{len(map[0]) - 1}', weight = 'weight')
print(cost)
