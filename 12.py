#!/usr/bin/python

import networkx as nx

def load_data():
    with open('12.txt') as file:
        data = [line.rstrip() for line in file.readlines()]
    return data

def find_node(label, tree):
    selected_index = -1
    for index, item in enumerate(tree):
        if item.label == label:
            selected_index = index
            break
    return selected_index

def build_graph(rules):
    graph = nx.Graph()
    for rule in rules:
        part = rule.split('-')
        graph.add_edge(part[0], part[1])
    return graph

def step_path(graph, node, end, path):
    paths = []
    for n in graph.neighbors(node):
        if n == end:
            paths.append(path + ',' + n)
            return
        elif path.find(f'{node},{n}') < 0:
            return node + ',' + step_path(graph, n, end, path)

def find_paths(graph, start, end):
    pathList = []
    path = start + ','
    for n in graph.neighbors(start):
        pathList.append(step_path(graph, n, end, path))
    return pathList

rules = load_data()
graph = build_graph(rules)
print(list(graph.nodes))
start = [n for n in graph.nodes if n == 'start'][0]
end = [n for n in graph.nodes if n == 'end'][0]
all_paths = find_paths(graph, 'start', 'end')
print(all_paths)
# for p in all_paths:
#     print(p)