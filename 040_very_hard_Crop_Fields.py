"""
Crop Fields
You're given a 2D list / matrix of a crop field. Each crop needs a water source. Each water source hydrates the 8 tiles around it. With "w" representing a water source, and "c" representing a crop, is every crop hydrated?

Examples
crop_hydrated([
  [ "w", "c" ],
  [ "w", "c" ],
  [ "c", "c" ]
])) # ➞ True

crop_hydrated([
  [ "c", "c", "c" ]
])) # ➞ False
# There isn"t even a water source.

crop_hydrated([
  [ "c", "c", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "c", "c", "c", "c" ],
  [ "c", "w", "c", "c" ]
])) # ➞ False
Notes
"w" on its own should return True, and "c" on its own should return False.

print(crop_hydrated([
  [ "w", "w" ],
  [ "w", "c" ],
  [ "c", "c" ],
  [ "c", "w" ],
  [ "c", "w" ]
])) #, True)) #
​
print(crop_hydrated([
  [ "c", "w", "w", "w", "c" ],
  [ "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "w", "c" ]
])) #, True)) #
​
print(crop_hydrated([
  [ "c", "w" ]
])) #, True)) #
​
print(crop_hydrated([
  [ "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "w", "c" ]
])) #, True)) #
​
print(crop_hydrated([
  [ "c", "c", "c" ],
  [ "w", "w", "c" ],
  [ "c", "c", "c" ],
  [ "w", "w", "c" ],
  [ "c", "c", "c" ],
  [ "c", "c", "c" ],
  [ "c", "w", "c" ]
  """
  
def crop_hydrated(field):
    
    # 畑のサイズを取得
    rows = len(field)
    cols = len(field[0]) if rows > 0 else 0
    
    # 水("w")の位置を取得
    water_positions = []
    crop_positions = set()
    
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == "w":
                water_positions.append((r, c))
            elif field[r][c] == "c":
                crop_positions.add((r,c))
    
    # 8方向（上下左右・斜め）の移動リスト
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    # 潤った作物の位置を保存
    hydrated_crops = set()
    
    for wr, wc in water_positions:
        for dr, dc in directions:
            nr, nc = wr + dr, wc + dc
            if 0 <= nr < rows and 0 <= nc < cols and field[nr][nc] == "c":
                hydrated_crops.add((nr, nc))
    
    # すべての作物が潤っているかを判定
    return crop_positions <= hydrated_crops 
                
    
    
    

    


print(crop_hydrated([
  [ "w", "w" ],
  [ "w", "c" ],
  [ "c", "c" ],
  [ "c", "w" ],
  [ "c", "w" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "w", "w", "w", "c" ],
  [ "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "w", "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "w" ]
])) #, True)) #

print(crop_hydrated([
  [ "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "w", "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "c", "c" ],
  [ "w", "w", "c" ],
  [ "c", "c", "c" ],
  [ "w", "w", "c" ],
  [ "c", "c", "c" ],
  [ "c", "c", "c" ],
  [ "c", "w", "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "c", "c" ],
  [ "w", "w", "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "w", "w", "c", "c", "w", "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "w", "c", "c", "w", "w" ],
  [ "c", "c", "w", "c", "c", "c" ],
  [ "w", "c", "c", "c", "c", "w" ],
  [ "c", "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "w", "w" ]
])) #, True)) #

print(crop_hydrated([
  [ "c" ],
  [ "w" ],
  [ "c" ],
  [ "c" ],
  [ "w" ],
  [ "c" ]
])) #, True)) #

print(crop_hydrated([
  [ "c", "c", "w", "w", "c", "c", "c" ],
  [ "c", "w", "c", "w", "w", "c", "w" ],
  [ "w", "w", "c", "w", "c", "c", "c" ]
])) #, True)) #


print(crop_hydrated([
  [ "c", "c", "w", "c", "c", "w", "c", "w" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "c", "c", "c", "c", "w", "c" ],
  [ "c", "w", "c", "c", "w", "c", "w" ],
  [ "c", "c", "c", "w", "c", "w", "c" ],
  [ "w", "w", "c", "c", "c", "c", "c" ],
  [ "c", "c", "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "w", "c", "c" ],
  [ "w", "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "c", "c", "c", "w" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "w", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "c", "c", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "w", "w", "c", "c" ],
  [ "c", "w", "c", "c" ],
  [ "c", "c", "w", "c" ],
  [ "c", "c", "w", "w" ],
  [ "c", "c", "c", "w" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "w" ],
  [ "c", "c", "c", "c", "w", "c" ],
  [ "c", "w", "w", "c", "c", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "c", "c", "c", "c", "w", "c" ],
  [ "w", "c", "c", "c", "c", "c", "w" ],
  [ "c", "c", "c", "c", "c", "c", "c" ],
  [ "c", "w", "w", "c", "c", "w", "w" ],
  [ "c", "c", "w", "c", "w", "c", "c" ],
  [ "w", "c", "c", "c", "w", "c", "c" ],
  [ "c", "c", "c", "c", "w", "c", "c" ],
  [ "w", "c", "c", "c", "c", "c", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "w", "c", "c", "w", "c", "c", "c", "w" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "c", "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "w", "w", "w", "c" ],
  [ "w", "c", "c", "w", "w", "c", "c", "c", "w" ],
  [ "c", "c", "c", "c", "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "c", "w", "c", "w" ],
  [ "c", "c", "c", "c", "c" ],
  [ "w", "c", "w", "c", "c" ],
  [ "c", "w", "w", "c", "c" ],
  [ "c", "c", "c", "c", "w" ],
  [ "c", "c", "c", "w", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "w", "c", "c", "c", "w", "w", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c", "c", "c" ],
  [ "w", "c", "c", "c", "c", "c", "w", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "w", "w", "c", "c", "w" ],
  [ "c", "c", "c", "c", "c" ],
  [ "c", "c", "w", "c", "c" ],
  [ "w", "c", "c", "w", "w" ],
  [ "c", "c", "w", "c", "c" ],
  [ "c", "c", "w", "c", "c" ],
  [ "c", "c", "c", "w", "c" ]
])) #, False)) #

print(crop_hydrated([
  [ "c", "c", "w", "c", "c", "w" ],
  [ "c", "w", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "w", "c", "c" ],
  [ "c", "c", "c", "c", "w", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ],
  [ "c", "c", "c", "c", "c", "c" ]
])) #, False)) #

# By Harith Shah