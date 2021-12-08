#!/usr/bin/python3

inputs = []
outputs = []

def load_data(inputs, outputs):
    with open('8.txt') as file:
        data = file.readlines()
        for input in data:
            part = input.split(' | ')
            inputs.append([line.strip() for line in part[0].split()])
            outputs.append([line.strip() for line in part[1].split()])
    return input

load_data(inputs, outputs)

def get_mapping(input):
    candidate = [[] for x in range(0, 8)]

def part_one():
    easy_digits = 0
    for output in outputs:
        for digit in output:
            if (len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
                easy_digits += 1
    print(easy_digits)

part_one()