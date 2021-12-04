#!/usr/bin/python3


numbers = []
boards = []


def load_data(numbers, boards):
    board = []
    n = 0
    with open('4.txt') as file:
        input = file.readlines()
    for line in input:
        if n == 0:
            number_list = line.split(',')
            numbers.extend(number_list)
        elif line.strip() == '':
            if n > 1:
                boards.append(board)
                board = []
        else:
            board.append(line.strip().split())
        n += 1
    boards.append(board)

def mark_numbers(boards, number):
    for board in boards:
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col == number:
                    board[r][c] = 'X'

def is_winner(board):
    return has_winning_row(board) or has_winning_column(board)

def has_winning_row(board):
    for r in range(5):
        win = True
        for c in range(5):
            win = win and board[r][c] == 'X'
        if win:
            return win
    return False

def has_winning_column(board):
    for c in range(5):
        win = True
        for r in range(5):
            win = win and board[r][c] == 'X'
        if win:
            return win
    return False

def get_score(number, board):
    total = 0
    for r in range(5):
        for c in range(5):
            if board[r][c] != 'X':
                total += int(board[r][c])
    return int(number) * total

def run1(numbers, boards):
    for number in numbers:
        print(number)
        mark_numbers(boards, number)
        for board in boards:
            if is_winner(board):
                return get_score(number, board)

def run2(numbers, boards):
    for number in numbers:
        print(number)
        mark_numbers(boards, number)
        for board_index, board in enumerate(boards):
            if is_winner(board):
                boards.pop(board_index)
                print(f'{len(boards)} boards left...')
                if(len(boards) == 0):
                    return get_score(number, board)


load_data(numbers, boards)
score = run2(numbers, boards)
print(score)