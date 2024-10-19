"""
Queen Threat
Create a function that takes a character from a to h as the column number and an integer from 1 to 8 as the row number which together represent the location of a queen on a normal-sized chess board. Return this two dimensional 8x8 list.

This list must consist of zeroes and ones. The ones are placed in positions where the queen can move in one move and zeroes represent positions on the board where it cannot.

Examples
check_board("a", 1) ➞ [
  [1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1]
]

check_board("h", 4) ➞ [
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1]
]

check_board("c", 8) ➞ [
  [1, 1, 0, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0]
]
Notes
The queens' current position is a zero as it is impossible to move to this position during one turn, because the queen is already there.
"""
import string

def check_board(col, row):

    matrix = [[0 for _ in range(8)] for _ in range(8)]

    col = string.ascii_lowercase.index(col)
    row = 8 - int(row)

    for i in range(8):
        if i != row:
            matrix[i][col] = 1
        if i != col:
            matrix[row][i] = 1

    for i in range(1, 8):
        if row - i >= 0 and col - i >= 0:
            matrix[row - i][col-i] = 1
        if row - i >= 0 and col + i < 8:
            matrix[row - i][col + i] = 1
        if row + i < 8 and col - i >= 0:
            matrix[row + i][col - i] = 1
        if row + i < 8 and col + i < 8:
            matrix[row + i][col + i] = 1

    return matrix

print(check_board('a',5))
print(check_board('f',1))
print(check_board('d',8))
print(check_board('b',3))
print(check_board('h',7))
print(check_board('c',4))
print(check_board('g',2))
print(check_board('e',6))
