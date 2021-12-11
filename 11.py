#!/usr/bin/python3

def load_data():
    data = []
    with open('11.txt') as file:
        input = file.readlines()
        for line in input:
            data.append([int(char) for char in line.strip()])
    return data

def print_grid(input):
    for row in input:
        for col in row:
            print(col, end='')
        print('')

def energy_increase(input):
    for r, row in enumerate(input):
        for c, col in enumerate(row):
            input[r][c] += 1

def resolve_flashes(input, flash_count):
    total = 0
    while True:
        this_pass = 0
        for r, row in enumerate(input):
            for c, col in enumerate(row):
                if input[r][c] > 9:
                    this_pass += 1
                    input[r][c] = 0
                    flash_increment(r, c, input)
        if this_pass == 0:
            break
        total += this_pass
    return total
                    
def flash_increment(r, c, input):
    for win_r in range(-1, 2):
        for win_c in range(-1, 2):
            if r + win_r < 0 or r + win_r >= len(input):
                continue
            if c + win_c < 0 or c + win_c >= len(input[0]):
                continue
            if input[r + win_r][c + win_c] > 0:
                input[r + win_r][c + win_c] += 1  
    
input = load_data()
flash_count = 0
step = 0
while(True):
    step += 1
    energy_increase(input)
    step_count = resolve_flashes(input, flash_count)
    if step_count == 100:
        break
print(flash_count)
print(step)