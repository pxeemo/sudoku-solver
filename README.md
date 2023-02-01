# Sudoku solver

This is a simple solver for Sudoku Game written in Python.
Note that it just solves level easy of Sudoku

## Installation

Just clone this repository:
```bash
git clone https://github.com/pexemo/sudoku-solver.git
cd sudoku-solver
```

### Requirments are:
- Python
- NumPy

## Usage

First make a text file like sample file (or just edit it) and enter your board data.

### SYNOPSIS
```man
python main.py [-u show unsolved] file
```
Example:
```
$ python3 main.py sample_board.txt

Your solved board:

┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓
┃ 9 │ 6 │ 3 ┃ 8 │ 1 │ 7 ┃ 5 │ 4 │ 2 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 8 │ 7 │ 1 ┃ 5 │ 4 │ 2 ┃ 6 │ 9 │ 3 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 2 │ 4 │ 5 ┃ 9 │ 3 │ 6 ┃ 8 │ 1 │ 7 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ 5 │ 3 │ 9 ┃ 4 │ 6 │ 1 ┃ 7 │ 2 │ 8 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 4 │ 1 │ 6 ┃ 7 │ 2 │ 8 ┃ 3 │ 5 │ 9 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 7 │ 8 │ 2 ┃ 3 │ 5 │ 9 ┃ 1 │ 6 │ 4 ┃
┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫
┃ 3 │ 2 │ 7 ┃ 6 │ 9 │ 5 ┃ 4 │ 8 │ 1 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 1 │ 5 │ 4 ┃ 2 │ 8 │ 3 ┃ 9 │ 7 │ 6 ┃
┠───┼───┼───╂───┼───┼───╂───┼───┼───┨
┃ 6 │ 9 │ 8 ┃ 1 │ 7 │ 4 ┃ 2 │ 3 │ 5 ┃
┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛
```
