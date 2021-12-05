#!/usr/bin/python3

def load_data():
    with open('5.txt') as file:
        data = [line.rstrip() for line in file.readlines()]
    return data

def get_dimension(input):
    max_x = 0
    max_y = 0
    for line in input:
        part = line.split(' -> ')
        start = part[0].split(',')
        end = part[1].split(',')
        if int(start[0]) > max_x:
            max_x = int(start[0])
        if int(end[0]) > max_x:
            max_x = int(end[0])
        if int(start[1]) > max_y:
            max_y = int(start[1])
        if int(end[1]) > max_y:
            max_y = int(end[1])
    return [max_x, max_y]

def build_field(data):
    field = []
    for x in range(dimensions[1] + 1):
        col = []
        for y in range(dimensions[0] + 1):
            col.append(0)
        field.append(col)
    return field

def draw_vertical_line(field, x1, y1, y2):
    for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
        field[int(x1)][y] += 1

def draw_horizontal_line(field, x1, x2, y1):
    for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
        field[x][int(y1)] += 1

def draw_diagonal_line(field, x1, y1, x2, y2):
    directionX = 1
    directionY = 1
    if(int(x1) > int(x2)):
        directionX = -1
    if(int(y1) > int(y2)):
        directionY = -1
    for n in range(abs(int(x1) - int(x2)) + 1):
        field[int(x1) + (directionX * n)][int(y1) + (directionY * n)] += 1

def map_field(data, field):
    for line in data:
        part = line.split(' -> ')
        x1 = part[0].split(',')[0]
        y1 = part[0].split(',')[1]
        x2 = part[1].split(',')[0]
        y2 = part[1].split(',')[1]
        if(x1 == x2):
            draw_vertical_line(field, x1, y1, y2)
        elif(y1 == y2):
            draw_horizontal_line(field, x1, x2, y1)
        else:
            draw_diagonal_line(field, x1, y1, x2, y2)

def danger_points(field):
    total = 0
    for row in field:
        for col in row:
            if col > 1:
                total += 1
    return total

def print_field(field):
    for row in field:
        for col in row:
            if col == 0:
                print('.', end = '')
            else:
                print(col, end = '')
        print('')

data = load_data()
dimensions = get_dimension(data)
print(dimensions)
field = build_field(data)
# print(field)
map_field(data, field)
print_field(field)
print(danger_points(field))
