"""
Chain Reaction (Part #2)
This is a sequel to Chain Reaction (Part #1), with the same setup, but a different flavor.

As in the previous part, you will be given a rectangular array representing a "map" with three types of spaces:

"+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
"x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
Empty spaces "0".
The goal is simple: given a map, return the minimum number of bombs that need to be set off for all bombs to be destroyed by the chain reaction.

Let's look at some examples:

[
  ["+", "+", "+", "0", "+", "+", "+"],
  ["+", "+", "+", "0", "0", "+", "+"]
]
For the map above, the answer is 2; to explode all bombs you just need to set off one "+" bomb in the right cluster and one in the left cluster.

[
  ["x", "0", "x"],
  ["x", "x", "x"]
]
For the map above, the answer is 3; clearly setting off the three bottom "x" bombs is enough, and no less than three bombs suffice.

[
  ["x", "x", "x", "0", "x"],
  ["x", "x", "x", "x", "x"],
  ["x", "x", "x", "0", "x"]
]
For the map above, the answer is 3; setting off the three rightmost bombs in the middle row will do the trick.

Examples
min_bombs_needed([
  ["+", "+", "+", "0", "+", "+", "+"],
  ["+", "+", "+", "0", "0", "+", "+"]
]) ➞ 2

min_bombs_needed([
  ["x", "0", "x"],
  ["x", "x", "x"]
]) ➞ 3

min_bombs_needed([
  ["x", "x", "x", "0", "x"],
  ["x", "x", "x", "x", "x"],
  ["x", "x", "x", "0", "x"]
]) ➞ 3
Notes
Note that both "+" and "x" bombs have an "explosion range" of 1.
To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be part 3!
Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.
"""

def dfs(grid, visited, x, y, bomb_type):
    # stackを使って深さ優先探索を行う
    stack = [(x, y)]

    # "+"爆弾と"x"爆弾の隣接セルの方向を設定
    if bomb_type == '+':
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 上下左右
    else: # bomb_type == 'x'
        directions = [(1, 1),(-1, -1),(1, -1),(-1, 1)] # 対角線

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == bomb_type:
                visited[nx][ny] = True
                stack.append((nx, ny))


def min_bombs_needed(grid):
    rows, cols = len(grid), len(grid[0])
    # 訪問済みかどうかを記載するリスト
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # 爆弾の種類を判定する
    if '+' in grid[0] or '+' in grid[1]:
        bomb_type = '+'
    else:
        bomb_type = 'x'

    cluster_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == bomb_type and not visited[i][j]:
                visited[i][j] = True
                dfs(grid, visited, i, j, bomb_type)
                cluster_count += 1

    return cluster_count

print(min_bombs_needed(
[['0', '+', '+', '0', '+'],
 ['+', '0', '+', '+', '0'],
 ['+', '+', '0', '0', '+']]))

print(min_bombs_needed(
[['+', '+', '0', '+', '+'],
 ['+', '0', '+', '0', '+'],
 ['0', '+', '+', '+', '0'],
 ['+', '0', '+', '0', '+'],
 ['+', '+', '0', '+', '+']]))


print(min_bombs_needed(
[['x', 'x', 'x', '0', 'x'],
 ['x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', '0', 'x']]))


print(min_bombs_needed(
[['x', '0', 'x', '0', 'x'],
 ['0', 'x', 'x', 'x', '0'],
 ['x', '0', 'x', '0', 'x'],
 ['0', 'x', 'x', 'x', '0'],
 ['x', '0', 'x', '0', 'x']]))