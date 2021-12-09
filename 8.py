#!/usr/bin/python3

inputs = []
outputs = []
digits = { 'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9 }
signals = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]

def load_data(inputs, outputs):
    with open('8.txt') as file:
        data = file.readlines()
        for input in data:
            part = input.split(' | ')
            inputs.append([line.strip() for line in part[0].split()])
            outputs.append([line.strip() for line in part[1].split()])
    return input

load_data(inputs, outputs)

def seg_frequencies(glyph_list):
    frequencies = {}
    for glyph in glyph_list:
        for char in glyph:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    return frequencies

def seg_a(inputs):
    one = [s for s in inputs if len(s) == 2][0]
    seven = [s for s in inputs if len(s) == 3][0]
    ones = [char for char in one]
    sevens = [char for char in seven]
    seg_a = [char for char in sevens if char not in ones][0]
    return seg_a

def seg_by_frequency(frequencies, value):
    return list(frequencies.keys())[list(frequencies.values()).index(value)]

def seg_by_frequency_except(frequencies, value, excluded):
    for key in frequencies.keys():
        if frequencies[key] == value and key != excluded:
            return key
def seg_d(inputs):
    candidates = [glyph for glyph in inputs if len(glyph) == 6 or len(glyph) == 5 or len(glyph) == 3 or len(glyph) == 2]
    f = seg_frequencies(candidates)
    return list(f.keys())[list(f.values()).index(5)][0]

def part_one():
    easy_digits = 0
    for output in outputs:
        for digit in output:
            if (len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
                easy_digits += 1
    print(easy_digits)

def translate(outputs, segment):
    translated_output = []
    glyph = [x for x in outputs]
    for g in glyph:
        translated = ''
        for signal in g:
            translated += segment[signal]
        translated_output.append(''.join(sorted(translated)))
    return translated_output

def decode(output, digits):
    return (digits[output[0]] * 1000) + (digits[output[1]] * 100) + (digits[output[2]] * 10) + digits[output[3]]

total = 0
i = 0
for input in inputs:
    freq = seg_frequencies(input)
    segment = {}
    segment['a'] = seg_a(input)
    segment['b'] = seg_by_frequency(freq, 6)
    segment['c'] = seg_by_frequency_except(freq, 8, segment['a'])
    segment['d'] = seg_d(input)
    segment['e'] = seg_by_frequency(freq, 4)
    segment['f'] = seg_by_frequency(freq, 9)
    segment['g'] = seg_by_frequency_except(freq, 7, segment['d'])
    map = { v: k for k, v in segment.items() }
    translated_output = translate(outputs[i], map)
    decoded_output = decode(translated_output, digits)
    total += decoded_output
    i += 1
print(f'Total: {total}')