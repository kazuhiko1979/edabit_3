"""
Right Rotation
Create a function which takes 2 parameters:

A matrix mat with m rows and n columns, containing data of any type.
An optional integer parameter turns giving the number of clockwise 90 degree rotations by which to transform the matrix (defaults to 1).
The function should return a new matrix with the elements rotated clockwise or counter-clockwise by the number of turns given.

For positive integers: 1 turn = 90° clockwise, 2 turns = 180° clockwise, 3 turns = 270° clockwise, 4 turns = 360° clockwise, etc.

For negative integers: -1 turn = 90° counter-clockwise, -2 turns = 180° counter-clockwise, -3 turns = 270° counter-clockwise, -4 turns = 360° counter-clockwise, etc.

Examples
rotate_matrix([
  [1,  2,  3,  4],
  [5,  6,  7,  8],
  [9, 10, 11, 12]
]) ➞ [
  [ 9, 5, 1],
  [10, 6, 2],
  [11, 7, 3],
  [12, 8, 4]
]
# A clockwise rotation.
# Left to right columns become rows in bottom to top order.


rotate_matrix([["+", "-"], ["*", "/"]], -1) ➞ [["-", "/"], ["+", "*"]]
# A counter-clockwise rotation.
# Right to left columns become rows in top to bottom order.


rotate_matrix([[1, 2, 3], [4, 5, 6]], 4) ➞ [[1, 2, 3], [4, 5, 6]]
# A 360° turn returns all elements to their original positions.
Notes
All given matrices (2-dimensional lists) will have at least 1 row and at least 1 column.
Do not mutate the original matrix, the return value should be a new 2-dimensional list with values copied from the original list.
Do not import any libraries - the challenge is to come up with your own solution.
Make sure your solution is efficient enough to cope with a large number of turns
You must provide a default value for the turns parameter.
"""
from typing import List


def rotate_matrix(matrix: List[List[int]], turns: int = 1) -> List[List[int]]:
    # 正負に関わらず4回転で元に戻るので、-4から3の範囲に正規化
    actual_turns = turns % 4
    # 負の場合は左回転を右回転に変換（例：-1 → 3）
    if actual_turns < 0:
        actual_turns = actual_turns + 4

    # 回転が0回の場合は、そのまま返す
    if actual_turns == 0:
        return matrix

    M = len(matrix)  # 行数
    N = len(matrix[0])  # 列数
    current = matrix

    # actual_turns回数分だけ90度回転を繰り返す
    for _ in range(actual_turns):
        # 新しい配列を作成（N×M）
        result = [[0 for _ in range(M)] for _ in range(N)]

        # 90度右回転の処理
        for i in range(M):
            for j in range(N):
                result[j][M - 1 - i] = current[i][j]

        # 次の回転のために現在の結果を保持
        current = result
        # 次の回転のためにMとNを入れ替え
        M, N = N, M

    return current
# def rotate_matrix(matrix, turns=1):
#
#     actual_turns = turns % 4
#
#     if actual_turns < 0:
#         actual_turns = actual_turns + 4
#
#     if actual_turns == 0:
#         return matrix
#
#     rows = len(matrix)
#     columns = len(matrix[0]) if rows > 0 else 0
#
#     current = matrix
#
#     for _ in range(actual_turns):
#         result = [[None for _ in range(rows)] for _ in range(columns)]
#
#         for i in range(rows):
#             for j in range(columns):
#                 result[j][rows-1-i] = current[i][j]
#
#         current = result
#
#         rows, columns = columns, rows
#
#     return current



mat1 = [[1,2,3], [4, 5, 6]]
mat2 = [[1,2,3,4,5,6,7,8,9]]

print(rotate_matrix(mat1)) #, [[4,1], [5,2], [6,3]])
print(rotate_matrix(mat1, -1)) #, [[3,6], [2,5], [1,4]])
print(rotate_matrix(mat1, 2)) #, [[6,5,4], [3,2,1]])
print(rotate_matrix(mat1, 4)) # , [[1,2,3], [4, 5, 6]])
print(rotate_matrix(mat2, 1)) #, [[1],[2],[3],[4],[5],[6],[7],[8],[9]])
print(rotate_matrix(mat2, 2)) #, [[9,8,7,6,5,4,3,2,1]])
print(rotate_matrix(mat2, 3)) #, [[9],[8],[7],[6],[5],[4],[3],[2],[1]])
print(rotate_matrix([['+','-'], ['*','/']], -1)) #, [['-','/'], ['+','*']])
print(rotate_matrix([
    ['#', '#', '#', '|', '*', '*', '*'], 
    ['#', '#', '#', '|', '*', '*', '*'], 
    ['#', '#', '#', '|', '*', '*', '*'], 
    ['-', '-', '-', '|', '-', '-', '-'], 
    ['$', '$', '$', '|', '&', '&', '&'], 
    ['$', '$', '$', '|', '&', '&', '&'], 
    ['$', '$', '$', '|', '&', '&', '&']], -5)) #,[
#     ['*', '*', '*', '-', '&', '&', '&'],
#     ['*', '*', '*', '-', '&', '&', '&'],
#     ['*', '*', '*', '-', '&', '&', '&'],
#     ['|', '|', '|', '|', '|', '|', '|'],
#     ['#', '#', '#', '-', '$', '$', '$'],
#     ['#', '#', '#', '-', '$', '$', '$'],
#     ['#', '#', '#', '-', '$', '$', '$']])
print(rotate_matrix([['in','mainly','plain'], ['rain','falls','the'], ['The','Spain','on']], 4097)) #, [['The','rain','in'], ['Spain','falls','mainly'], ['on','the','plain']])







