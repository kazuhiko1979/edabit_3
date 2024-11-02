"""
Switch on the Gravity
Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.

Examples
switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "#", "-"],
  ["-", "-", "-", "-"],
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "#", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "#", "#", "-"],
  ["#", "-", "-", "#", "#", "-"],
  ["-", "#", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"],
  ["-", "#", "-", "#", "#", "-"],
  ["#", "#", "#", "#", "#", "-"]
]
Notes
Each block falls individually, meaning there are no rigid objects. Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.
"""
def switch_gravity_on(grid):
    # 転置行列を使って列ごとの処理を簡略化
    columns = list(zip(*grid))

    # 各列に重力を適用して再度転置
    return list(map(list, zip(*[apply_gravity_to_column(col) for col in columns])))

def apply_gravity_to_column(column):
    # '#'の数をカウント
    block_count = column.count('#')
    # 新しい列を作成：上部が'-'、下部が'#'
    return ['-'] * (len(column) - block_count) + ['#'] * block_count




# def switch_gravity_on(grid):
#     # 列数を取得
#     column_count = len(grid[0])
#
#     # 各列に対して処理を行う
#     for col in range(column_count):
#         column = [grid[row][col] for row in range(len(grid))]
#
#         # '#'の位置を記録
#         blocks = []
#         for i in range(len(column)):
#             if column[i] == '#':
#                 blocks.append(i)
#
#         # 新しい列を作成(全て'-'で初期化)
#         new_column = ['-'] * len(column)
#         for i, pos in enumerate(blocks):
#             new_pos = len(column) - len(blocks) + i
#             new_column[new_pos] = '#'
#
#         # 元のgridの列を更新
#         for i in range(len(grid)):
#             grid[i][col] = new_column[i]
#
#     return grid


print(switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]))
# ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "#", "#", "-"]
# ]


print(switch_gravity_on([
  ["-", "#", "#", "#", "#", "-"],
  ["#", "-", "-", "#", "#", "-"],
  ["-", "#", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"]
]))
# ➞ [
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "#", "-", "#", "#", "-"],
#   ["#", "#", "#", "#", "#", "-"]
# ])