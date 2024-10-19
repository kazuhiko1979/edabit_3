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


def check_board(col, row):
    col_idx = ord(col) - ord('a')
    row_idx = 8 - int(row)

    board = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if i == row_idx or j == col_idx or abs(i - row_idx) == abs(j - col_idx):
                board[i][j] = 1

    board[row_idx][col_idx] = 0

    return board


# import string
#
# BOARD_SIZE = 8
#
# def create_empty_board():
#      return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
#
# def get_queen_position(col, row):
#     return string.ascii_lowercase.index(col), BOARD_SIZE - int(row)
#
#
# def mark_horizontal_vertical(board, row, col):
#     for i in range(BOARD_SIZE):
#         if i != col:
#             board[row][i] = 1
#         if i != row:
#             board[i][col] = 1
#
# def mark_diagonals(board, row, col):
#     for i in range(BOARD_SIZE):
#         for j in range(BOARD_SIZE):
#             if abs(row - i) == abs(col -j) and (i != row or j != col):
#                 board[i][j] = 1
#
#
# def check_board(col, row):
#     board = create_empty_board()
#     queen_col, queen_row = get_queen_position(col, row)
#     mark_horizontal_vertical(board, queen_row, queen_col)
#     mark_diagonals(board, queen_row, queen_col)
#     return board




# import string
#
# def check_board(col, row):
#
#     matrix = [[0 for _ in range(8)] for _ in range(8)]
#
#     col = string.ascii_lowercase.index(col)
#     row = 8 - int(row)
#
#     for i in range(8):
#         if i != row:
#             matrix[i][col] = 1
#         if i != col:
#             matrix[row][i] = 1
#
#     for i in range(1, 8):
#         if row - i >= 0 and col - i >= 0:
#             matrix[row - i][col-i] = 1
#         if row - i >= 0 and col + i < 8:
#             matrix[row - i][col + i] = 1
#         if row + i < 8 and col - i >= 0:
#             matrix[row + i][col - i] = 1
#         if row + i < 8 and col + i < 8:
#             matrix[row + i][col + i] = 1
#
#     return matrix

print(check_board('a',5))
print(check_board('f',1))
print(check_board('d',8))
print(check_board('b',3))
print(check_board('h',7))
print(check_board('c',4))
print(check_board('g',2))
print(check_board('e',6))
