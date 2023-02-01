#!/bin/python
import numpy as np
import argparse

def board_reader(file):
    board = np.zeros((9,9), dtype=int)
    f = open(file, "r")
    next(f)
    for i in range(9):
        char = f.readline()
        for j in range(9):
            board[i][j] = char[j]
    return board

def pretty_board(board):
    board = board.reshape((81)).astype(np.str_)
    box = """
┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃ {} │ {} │ {} ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛
"""
    return box.format(*board)

def check_cell(board, row, colum, num):
    # check number exist in row
    if num in board[row]:
        return False

    # check number exist in colum
    for rows in board:
        if rows[colum] == num:
            return False

    # check number exist in square
    square_row = int(row / 3) * 3
    square_colum = int(colum / 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_colum, square_colum + 3):
            if board[i][j] == num:
                return False
    return True


def by_each(board):
    # function to check each cell
    for row in range(9):
        for colum in range(9):
            if board[row][colum] != 0:
                continue
            result = []
            for num in range(1, 10):
                result.append(check_cell(board, row, colum, num))

            if result.count(True) == 1:
                return row, colum, result.index(True) + 1

def by_row(board):
    # function to check by each row
    for num in range(1, 10):
        for row in range(9):
            result = []
            for colum in range(9):
                if board[row][colum] != 0:
                    result.append(False)
                    continue
                result.append(check_cell(board, row, colum, num))

            if result.count(True) == 1:
                return row, result.index(True), num

def by_square(board):
    # function to check by each square
    for num in range(1, 10):
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
                result.append(check_cell(board, row, colum, num))
            if result.count(True) == 1:
                row = (big_row * 3) + int(result.index(True) / 3)
                colum = (big_colum * 3) + (result.index(True) % 3)
                return row, colum, num

def by_colum(board):
    # function to check by each colum
    for num in range(1, 10):
        for colum in range(9):
            result = []
            for row in range(9):
                if board[row][colum] != 0:
                    result.append(False)
                    continue
                result.append(check_cell(board, row, colum, num))

            if result.count(True) == 1:
                return result.index(True), colum, num

def solve(board):
    while 0 in board:
        values = (by_row(board) or 
                  by_colum(board) or 
                  by_square(board) or 
                  by_each(board))
        if values == None:
            print("Can't solve all!")
            return board
        row, colum, number = values
        board[row][colum] = number
    return board

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the board text file")
parser.add_argument("-u","--unsolved", 
                    help="show the unsolved board",
                    action="store_true")
args = parser.parse_args()

unsolved_board = board_reader(args.file)
if args.unsolved:
    print("Your unsolved board:")
    print(pretty_board(unsolved_board))

solved_board = solve(unsolved_board)
print("Your solved board:")
print(pretty_board(solved_board))
