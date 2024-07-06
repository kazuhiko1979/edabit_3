"""
Infection of the Ones
Write a function that replaces every row and column that contains at least one 1 into a row/column that is filled entirely with 1s.

Solve this without returning a copy of the input list.

Examples
ones_infection([
  [0, 0, 1],
  [0, 0, 0],
  [0, 0, 0]
]) ➞ [
  [1, 1, 1],
  [0, 0, 1],
  [0, 0, 1]
]

ones_infection([
  [1, 0, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0]
]) ➞ [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 0]
]

ones_infection([
  [0, 1, 0, 1],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]) ➞ [
  [1, 1, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 1]
]
Notes
You must mutate the original matrix.
Input matrices will have at least row and one column.
Bonus: Solve this without using any higher-order function
"""
import numpy as np

def ones_infection(arr):

    rows = len(arr)
    cols = len(arr[0])

    indices = [(i, j) for i, row in enumerate(arr) for j, _ in enumerate(row)]
    zero_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for row, col in indices:
        row_list = arr[row]
        col_list = [arr[i][col] for i in range(rows)]

        if 1 in row_list or 1 in col_list:
            zero_matrix[row][col] = 1

    return zero_matrix



print(ones_infection([
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]))

print(ones_infection([
  [1, 0, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0]
]))


print(ones_infection([
  [0, 1, 0, 1],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]))