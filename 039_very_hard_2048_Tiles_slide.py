"""
2048 Tiles Slide
2048 is a game where you need to slide numbered tiles (natural powers of 2) up, down, left or right on a square grid to combine them in a tile with the number 2048.

The sliding procedure is described by the following rules:

Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid.
If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided.
If more than one variant of merging is possible, move direction shows one that will take effect.
Tile cannot merge with another tile more than one time.
Sliding is done almost the same for each direction and for each row/column of the grid, so your task is to implement only the left slide for a single row.

Examples
left_slide([2, 2, 2, 0]) ➞ [4, 2, 0, 0]
# Merge left-most tiles first.

left_slide([2, 2, 4, 4, 8, 8]) ➞ [4, 8, 16, 0, 0, 0]
# Only merge once.

left_slide([0, 2, 0, 2, 4]) ➞ [4, 4, 0, 0, 0]

left_slide([0, 2, 2, 8, 8, 8]) ➞ [4, 16, 8, 0, 0, 0]
Notes
Input row can be of any size (empty too).
Input row will contain only natural powers of 2 and 0 for empty tiles.
Keep trailing zeros in the output."""

def left_slide(row):
    # 0を除去して左詰め
    non_zero_row = [num for num in row if num != 0]
    
    merged = [False] * len(row)
    
    # 隣同士を合体
    i = 0
    while i < len(non_zero_row) - 1:
        if non_zero_row[i] == non_zero_row[i+1] and not merged[i] and not merged[i+1]:
            # 合体
            non_zero_row[i] *=2
            # 合体済みフラグを設定
            merged[i] = True
            # 次の要素を削除
            non_zero_row.pop(i+1)
            merged.pop(i+1)
        else:
            i += 1
            
    # 0を追加して元の長さに戻す
    non_zero_row += [0] * (len(row) - len(non_zero_row))
    
    return non_zero_row
        

print(left_slide([2, 2, 2, 0])) # [4, 2, 0, 0])
print(left_slide([2, 2, 4, 4, 8, 8])) # [4, 8, 16, 0, 0, 0])
print(left_slide([0, 2, 0, 2, 4])) # [4, 4, 0, 0, 0])
print(left_slide([0, 2, 2, 8, 8, 8])) # [4, 16, 8, 0, 0, 0])
print(left_slide([0, 0, 0, 0])) # [0, 0, 0, 0])
print(left_slide([0, 0, 0, 2])) # [2, 0, 0, 0])
print(left_slide([2, 0, 0, 0])) # [2, 0, 0, 0])
print(left_slide([8, 2, 2, 4])) # [8, 4, 4, 0])
print(left_slide([1024, 1024, 1024, 512, 512, 256, 256, 128, 128, 64, 32, 32])) # [2048, 1024, 1024, 512, 256, 64, 64, 0, 0, 0, 0, 0])