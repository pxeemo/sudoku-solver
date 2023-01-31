#!/bin/python
import numpy as np

def board_reader():
    board = np.zeros((9,9), dtype=int)
    f = open("board.txt", "r")
    next(f)
    i = 0
    while True:
        char = f.readline()
        j = 0
        for c in char:
            board[i][j] = c
            j += 1
            if j == 9:
                break
        i += 1
        if i == 9:
            i = 0
            break
    return board

board = board_reader()
print(board)


def check_cell(row, colum, n):
    # check_row
    if n in board[row]:
        return False

    # check_colum
    for rows in board:
        if rows[colum] == n:
            return False

    # check_square
    square_start_row = int(row / 3) * 3
    square_start_colum = int(colum / 3) * 3
    for i in range(square_start_row, square_start_row + 3):
        for j in range(square_start_colum, square_start_colum + 3):
            if board[i][j] == n:
                return False
    return True


def each_self():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                continue
            result = []
            for n in range(1, 10):
                result.append(check_cell(i, j, n))

            if result.count(True) == 1:
                board[i][j] = result.index(True) + 1

def each_row():
    for n in range(1, 10):
        for i in range(9):
            result = []
            for j in range(9):
                if board[i][j] != 0:
                    result.append(False)
                    continue
                result.append(check_cell(i, j, n))

            if result.count(True) == 1:
                board[i][result.index(True)] = n

def each_square():
    for n in range(1, 10):
        for big in range(9):
            big_row = int(big / 3)
            big_colum = big % 3
            result = []
            for small in range(9):
                small_row = int(small / 3)
                small_colum = small % 3
                row = big_row * 3 + small_row
                colum = big_colum * 3 + small_colum
                if board[row][colum] != 0:
                    result.append(False)
                    continue
                result.append(check_cell(row, colum, n))
            if result.count(True) == 1:
                row = (big_row * 3) + int(result.index(True) / 3)
                colum = (big_colum * 3) + (result.index(True) % 3)
                board[row][colum] = n


def each_colum():
    for n in range(1, 10):
        for j in range(9):
            result = []
            for i in range(9):
                if board[i][j] != 0:
                    result.append(False)
                    continue
                result.append(check_cell(i, j, n))

            if result.count(True) == 1:
                board[result.index(True)][j] = n

def solve():
    while np.count_nonzero(board == 0) > 4:
        tmp = board.copy()
        each_square()
        each_row()
        each_colum()
        each_self()
        if np.array_equal(tmp, board):
            break

solve()
print(*board,sep="\n")
