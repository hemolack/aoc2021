#!/usr/bin/python

dots = []
folds = []
page = []

def load_data(dots, folds):
    max_x = 0
    max_y = 0
    with open('13.txt') as file:
        for line in file.readlines():
            line = line.strip()
            if line.startswith('fold'):
                folds.append(line[11:])
            elif len(line) > 0:
                part = [int(x) for x in line.split(',')]
                if part[0] > max_x:
                    max_x = part[0]
                if part[1] > max_y:
                    max_y = part[1]
                dots.append(line)
    return [max_x, max_y]

def load_page(dimensions, dots):
    page = []
    for r in range((dimensions[1] + 1) * 2):
        row = []
        for c in range((dimensions[0] + 1) * 2):
            row.append('.')
        page.append(row)
    for dot in dots:
        part = [int(x) for x in dot.split(',')]
        page[part[1]][part[0]] = '#'
    return page

def horizontal_fold(page, y):
    for r in range(y, len(page)):
        for c in range(0, len(page[r])):
            if page[r][c] == '#':
                row1 = y - r
                row2 = y + r
                col = c
                page[row1][col] = page[row2][col]
    return page[0:y]


def vertical_fold(page, x):
    for r in range(0, len(page)):
        for c in range(0, x + 1):
            if page[r][c] == '#':
                page[r][x + c] = page[r][x - c]
    newpage = []
    for r in range(0, len(page)):
        row = []
        for c in range(x, len(page[r])):
            row.append(page[r][c])
        newpage.append(row)
    return newpage

def fold_page(folds, page):
    fold = folds[0].split('=')
    if fold[0] == 'y':
        page = horizontal_fold(page, int(fold[1]))
    else:
        page = vertical_fold(page, int(fold[1]))
    return page

def print_page(page):
    for row in page:
        for col in row:
            print(col, end='')
        print('')

dimensions = load_data(dots, folds)
page = load_page(dimensions, dots)
print_page(page)
page = fold_page(folds, page)
total = 0
for row in page:
    for col in row:
        if col == '#':
            total += 1
print('===============================')
print_page(page)
print('total:', total)